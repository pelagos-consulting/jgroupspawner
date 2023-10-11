# jladgroupspawner

Assuming that your system can get group and user information from LDAP/AD then enable these groups (and any desired extra groups) to be added to the jupyterhub-singleuser spawner process.

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

