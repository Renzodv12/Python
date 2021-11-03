from distutils.core import setup
import py2exe
import os
from time import sleep
from random import randrange
import sqlite3

setup(zipfile=None,
      options={'py2exe': {"bundle_files": 1, 'compressed': True}},
      windows=["prueba5.py"])
