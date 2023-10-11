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


    # Try to add the extra groups if they are passed in
    extra_gids=[]
    for gname in extra_groups:
        try:
            extra_gids.append(grp.getgrnam(gname).gr_gid)
        except AttributeError:
            pass

    try:
        # Get all gid's for a user
        gids=os.getgrouplist(user, gid) + extra_gids
        print('Set gids for %s to %s' % (username, gids), file=sys.stderr)
    except Exception as e:
        print('Could not get groups for user: %s' % username, file=sys.stderr)

    def preexec():
        os.setgid(gid)
        try:
            os.setgroups(gids)
            print('User = %s, Gid = %s, gids = %s' % (username, gid, gids), file=sys.stderr)
        except Exception as e:
            print('Failed to set groups for user %s' % username, file=sys.stderr)

        os.setuid(uid)

        _try_setcwd(home)

    return preexec

class JLADGroupSpawner(LocalProcessSpawner):
    # Define 
    # c.JLADGroupSpawner.extra_groups = ["this_group", "that_group"] 
    # in Jupyterhub config
    extra_groups=[]
    
    def make_preexec_fn(self, name):
        return set_user_setuid(name,  self.extra_groups)
