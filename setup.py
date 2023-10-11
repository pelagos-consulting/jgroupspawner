from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'JLAD Group Spawner'
LONG_DESCRIPTION = ('Jupyterhub spawner with support to get groups from LDAP and Active Directory '
        'as well as support for adding in extra_groups.')

# Setting up
setup_args =dict(
	name="jladgroupspawner", 
        version=VERSION,
        author="Toby Potter",
        author_email="tobympotter@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'jupyterhub', 'spawner'],
        classifiers= [
            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',
            'Intended Audience :: Science/Research',
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
        ]
        #entry_points={
        #    'jupyterhub.spawners' : [
        #        'jladgs=jladgroupspawner:JLADGroupSpawner'
        #    ]
        #}
)

def main():
    setup(**setup_args)

if __name__ == '__main__':
    main()
