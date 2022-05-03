import os
import glob
import shutil

def clean_data(path, sub=True, participants=True):
    if sub:
        sub = 'sub-*'
        files = glob.glob(os.path.join(path, sub))
        for f in files:
            if os.path.isdir(f):
                shutil.rmtree(f)

    if participants:
        files = glob.glob(os.path.join(path, 'participants.*'))
        for f in files:
            if os.path.isfile(f):
                os.remove(f)
