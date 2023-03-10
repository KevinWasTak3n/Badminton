import os
import shutil

def makeDir(path):
    os.mkdir(path)

def removeDir(path):
    shutil.rmtree(path)