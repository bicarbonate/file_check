# -*- coding: utf-8 -*-

from pathlib import *
monitor_files = []

adr01_file = Path("/home/skeer/Documents/Projects/Python_temp/home/adr01/upload/monitor.20170701.pgp")
if adr01_file.is_file():
    monitor_files[0]
else:
    print("File does not exist")

    
chpt_file = Path("/home/skeer/Documents/Projects/Python_temp/home/chpt/upload/monitor.20170701.pgp")
if chpt_file.is_file():
    print("File exists")
else:
    print("File does not exist")
    
    
emb01_file = Path("/home/skeer/Documents/Projects/Python_temp/home/emb01/upload/monitor*.pgp")
if emb01_file.is_file():
    print("File exists")
else:
    print("File does not exist")
    
    
exp01_file = Path("/home/skeer/Documents/Projects/Python_temp/home/exp01/upload/monitor*.pgp")
if exp01_file.is_file():
    print("File exists")
else:
    print("File does not exist")
    
    
iix01_file = Path("/home/skeer/Documents/Projects/Python_temp/home/iix01/upload/monitor*.pgp")
if iix01_file.is_file():
    print('File exists')
else:
    print('File does not exist')
    
    

