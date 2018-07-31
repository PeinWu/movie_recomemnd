import sys

from fabric.colors import red
from fabric.api import local,task

@task(default=True)
def check():
    PY3 = sys.version_info[0]==True
    if not (PY3):
        print(red('Please install python3 to build the project'))
        quit()

@task
def clean():
    local('./bin/clean.py && fclear python')

@task(alias='i')
def install():
    check()
    local('pip3 install -r requirements.txt')

@task
def fix():
    check()
    local('yapf -ir .')

@task
def start():
    check()
    local('python3 -m moviebox.main')

@task
def dist():
    check()
    local('python3 setup.py sdist bdist_wheel')

