# jladgroupspawner

Assuming that your system can get group and user information from LDAP/AD then enable these groups (and any desired extra groups) to be added to the jupyterhub-singleuser spawner process.

## Installation

`pip install jladgroupspawner`

## In Jupyterhub config file

Set this parameter in your jupyterhub config file:

`c.JupyterHub.spawner_class = 'jladgroupspawner.JLADGroupSpawner'`

Then, if you would like to add additional groups (such as for GPU access etc), then add this line to the Jupyterhub config file:

`c.JLADGroupSpawner.extra_groups=["groupA", "groupB"]`
