#! /usr/bin/env python 3
import shutil

from termcolor import colored
from os.path import (exists,abspath)

green = 'green'
yellow = 'yellow'

distDir = abspath('dist')
buildDir = abspath('build')
eggDir = abspath('moviebox.egg-info')

if (exists(distDir)):
    # check is there is a directory exist
    shutil.rmtree(distDir)
    print(colored('Clean up '+distDir,green))

if (exists(buildDir)):
    shutil.rmtree(buildDir)
    print(colored('clearn up'+buildDir,yellow))

if (exists(eggDir)):
    shutil.rmtree(eggDir)
    print(colored('clearn up'+eggDir,green))
