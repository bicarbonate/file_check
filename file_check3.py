# -*- coding: UTF-8 -*-
# Ben Hart - SysAdmin Montana Interactive
# Jul 2017
# This file checks the chroot user directories for the Monitor customers uploads folders to
# verify the monthly files exist.

import glob
import os
from datetime import datetime


monitor_files = []

os.chdir("/home/skeer/Documents/Projects/Python_temp/home/adr01/upload/")
for file in glob.glob("*.pgp"):
    if os.path.isfile(file):
        last_modified_date = datetime.fromtimestamp(os.path.getmtime(file))
    else:
        last_modified_date = datetime.fromtimestamp(0)
    monitor_files.append("adr01 | " + file + (" | ") + str(last_modified_date) + "\n")

os.chdir("/home/skeer/Documents/Projects/Python_temp/home/chpt/upload/")
for file in glob.glob("*.pgp"):
    if os.path.isfile(file):
        last_modified_date = datetime.fromtimestamp(os.path.getmtime(file))
    else:
        last_modified_date = datetime.fromtimestamp(0)
    monitor_files.append("chpt | " + file + (" | ") + str(last_modified_date) + "\n")

os.chdir("/home/skeer/Documents/Projects/Python_temp/home/emb01/upload/")
for file in glob.glob("*.pgp"):
    if os.path.isfile(file):
        last_modified_date = datetime.fromtimestamp(os.path.getmtime(file))
    else:
        last_modified_date = datetime.fromtimestamp(0)
    monitor_files.append("emb01 | " + file + (" | ") + str(last_modified_date) + "\n")

os.chdir("/home/skeer/Documents/Projects/Python_temp/home/exp01/upload/")
for file in glob.glob("*.pgp"):
    if os.path.isfile(file):
        last_modified_date = datetime.fromtimestamp(os.path.getmtime(file))
    else:
        last_modified_date = datetime.fromtimestamp(0)
    monitor_files.append("exp01 | " + file + (" | ") + str(last_modified_date) + "\n")

os.chdir("/home/skeer/Documents/Projects/Python_temp/home/iix01/upload/")
for file in glob.glob("*.pgp"):
    if os.path.isfile(file):
        last_modified_date = datetime.fromtimestamp(os.path.getmtime(file))
    else:
        last_modified_date = datetime.fromtimestamp(0)
    monitor_files.append("iix01 | " + file + (" | ") + str(last_modified_date) + "\n")

print("\n".join(monitor_files))


 #   fromaddr = ("DZ@mt.gov")
  #  toaddrs = ("invalid.path@gmail.com")
