from setuptools import setup, find_packages

from shm import __version__


def readme():
    with open('README.md') as f:
        return f.read()


def requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()

setup(
    name='shm',
    version=__version__,
    description='Python implementation of simple hydrological model',
    long_description=readme(),
    long_description_content_type='text/markdown',
    author='Boney Joseph',
    author_email='',
    license='GNU GPLv3',
    install_requires=requirements(),
    packages=find_packages()
)
