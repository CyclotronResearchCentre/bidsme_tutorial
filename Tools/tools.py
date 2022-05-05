import os
import glob
import shutil

def clean_data(path, sub=True, participants=True):
    """
    Recursively removes all subject folders and participants tables
    from bids-like dataset

    Parameters:
    -----------
    path: str
        path to bids-like dataset
    sub: bool
        if True, removes all subject (sub-*) folders
    participants: bool
        if True, removes participants table (participants.*)
    """
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

    f = os.path.join(path, '__duplicated.tsv')
    if os.path.isfile(f):
        os.remove(f)
