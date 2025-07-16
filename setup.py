from setuptools import setup

setup(
    name='crackstorm',
    version='1.0',
    py_modules=['crackstorm'],
    entry_points={
        'console_scripts': [
            'crackstorm = crackstorm:main',
        ],
    },
    install_requires=[
        'paramiko',
    ],
    author='Jibin Kurian',
    description='CrackStorm – A Multi-Mode Password Cracker Tool',
)
