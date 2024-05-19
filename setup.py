from setuptools import setup, find_packages

setup(
    name='tsr',
    packages=find_packages(),
    install_requires=[
        line.strip() for line in open('requirements.txt') if line.strip()!=''
        ],
)