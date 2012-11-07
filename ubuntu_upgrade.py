#!/usr/bin/python
import os

command = 'sudo apt-get update && sudo apt-get upgrade'
print command
os.system(command)
