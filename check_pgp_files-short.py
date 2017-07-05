import glob
import os
from datetime import datetime


monitor_files = []
dirlist       = "adr01 chpt emb01 exp01 iix01".split()

def getLastMod(file):
    if os.path.isfile(file):
        return datetime.fromtimestamp(os.path.getmtime(file))
    else:
        return datetime.fromtimestamp(0)


for dirname in dirlist:
    path = '/home/skeer/Documents/Projects/Python_temp/home/' + dirname + '/upload/*.pgp'
    for file in glob.glob(path):
        monitor_files.append('{} | {} | {}'.format(dirname, file, str(getLastMod(file))))

print("\n".join(monitor_files))