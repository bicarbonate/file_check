# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from pathlib import Path
import os.path
#os.path.isfile()

#adr01_file = Path(/chroot/monitor/adr01/upload/)
#chpt_file = Path(/chroot/monitor/chpt/upload/monitor*.pgp)
#emb01_file = Path(/chroot/monitor/emb01/upload/)
#exp01_file = Path(/chroot/monitor/exp01/upload/)
#iix01_file = Path(/chroot/monitor/iix01/upload/)

adr01_file = Path(/home/bhart/Documents/Python/home/adr01/upload/monitor*.pgp)
if adr01_file.is_file():
    print('File exists')
 else:
     print('File dot not exist')
    
    
chpt_file = Path(/home/bhart/Documents/Python/home/chpt/upload/monitor*.pgp)
if adr01_file.is_file():
    print('File exists')
else:
    print('File does not exist')
    
    
emb01_file = Path(/home/bhart/Documents/Python/home/emb01/upload/monitor*.pgp)
if adr01_file.is_file():
    print('File exists')
else:
    print('File does not exist')
    
    
exp01_file = Path(/home/bhart/Documents/Python/home/exp01/upload/monitor*.pgp)
if adr01_file.is_file():
    print('File exists')
else:
    print('File does not exist')
    
    
iix01_file = Path(/home/bhart/Documents/Python/home/iix01/upload/monitor*.pgp)
if adr01_file.is_file():
    print('File exists')
else:
    print('File does not exist')
    
    

