from setuptools import find_packages
from setuptools import setup

setup(
    name='rc_car',
    version='0.0.0',
    packages=find_packages(
        include=('rc_car', 'rc_car.*')),
)
