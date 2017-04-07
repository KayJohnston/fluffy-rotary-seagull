import sys
from cx_Freeze import setup, Executable

setup(
    name = 'Password Self Setter',
    version = '1',
    description = 'Password Self Setter',
    executables = [Executable('selfset.py', base = 'Win32GUI')])
