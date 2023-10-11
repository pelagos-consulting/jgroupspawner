# jladgroupspawner

The default spawner in Jupyterhub doesn't seem to pick up groups that are not local, (i.e defined on a LDAP or AD server). So when a jupyterhub-singleuser notebook server instance is launched then it doesn't pick up all the groups that a user is part of. Furthermore, for LDAP/AD users it is sometimes desired behaviour to add local groups to the groups list for the purpose of accessing resources like GPU's etc.

This spawner uses the `os.getgrouplist` method to get available groups and sets them for the process that is running a singleuser notbook. You also have the option of defining a `pre_spawn_hook` function that sets any number of local extra groups that you would like to give the user access to.

## Installation

`pip install jladgroupspawner`

## In Jupyterhub config file

Set this parameter in your jupyterhub config file to use this spawner:

`c.JupyterHub.spawner_class = 'jladgroupspawner.JLADGroupSpawner'`

Then, if you would like to add additional groups (such as local groups for GPU access etc), then add these lines to the Jupyterhub config file:

```python
def pre_spawn_hook_fun(spawner):
    # Whatever groups you like to add
    spawner.extra_groups=["video", "render"]
  
c.Spawner.pre_spawn_hook = pre_spawn_hook_fun
```

