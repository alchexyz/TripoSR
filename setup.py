from setuptools import setup, find_packages

def requirements_from_file(file_name):
    reqs=[]
    deps=[]
    for s in open(file_name).read().splitlines():
        if s[:4]=='git+':
            deps.append(s[4:])
        else:
            reqs.append(s)
    return reqs, deps

setup(
    name='tsr',
    packages=find_packages(),
    install_requires=requirements_from_file('requirements.txt')[0],
    dependency_links=requirements_from_file('requirements.txt')[1]
)