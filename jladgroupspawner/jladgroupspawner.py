import os
import sys
import pwd
import grp
from subprocess import check_output
from jupyterhub.spawner import LocalProcessSpawner, _try_setcwd

def set_user_setuid(username, extra_groups):
    user = pwd.getpwnam(username)
    uid = user.pw_uid
    gid = user.pw_gid
    home = user.pw_dir
    gids = [gid]

    try:
        # Get all GID's for a user, put them into a set
        gids=set(os.getgrouplist(username, gid))
    except Exception as e:
        print(f'Could not use os.getgrouplist to get groups for {username}, error is: {repr(e)}', file=sys.stderr)

    # Try to add the extra groups if they are passed in
    for gname in extra_groups:
        try:
            # Try to add the extra groups to the set
            gids.add(grp.getgrnam(gname).gr_gid)
        except Exception as e:
            print(f'Error adding extra group {gname} to the set of groups, error is: {repr(e)}', file=sys.stderr)

    def preexec():
        os.setgid(gid)
        try:
            os.setgroups(list(gids))
            print('Set groups for user = %s, Gid = %s, gids = %s' % (username, gid, gids), file=sys.stderr)
        except Exception as e:
            print('Failed to set groups for user %s' % username, file=sys.stderr)

        os.setuid(uid)

        _try_setcwd(home)

    return preexec

class JLADGroupSpawner(LocalProcessSpawner):
    # Define a hook function in jupyterhub_config.py in order to set extra_groups
    # like this
    # def hook_fun(spawner):
    #     spawner.extra_groups=["video", "render"]
    # c.Spawner.pre_spawn_hook = hook_fun

    extra_groups=[]
    
    def make_preexec_fn(self, name):
        return set_user_setuid(name,  self.extra_groups)
