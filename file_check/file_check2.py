import glob
import os

def check_for_files(filepath):
    for filepath_object in glob.glob('/home/skeer/Documents/Projects/Python_temp/home/adr01/upload'):
        if os.path.isfile("monitor.*.pgp"):
            return True
            expression_if_true
            print('file found')
    return False

