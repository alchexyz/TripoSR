from setuptools import setup, find_packages

def requirements_from_file(file_name):
    return open(file_name).read()

setup(
    name='tsr',
    packages=find_packages(),
    install_requires=requirements_from_file('requirements.txt'),
)