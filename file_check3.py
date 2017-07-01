# -*- coding: UTF-8 -*-

import glob
import os

os.chdir("/home/skeer/Documents/Projects/Python_temp/home/adr01/upload/")
for file in glob.glob("*.pgp"):
    print(file)
    # noinspection PyUnresolvedReferences
    adr01.file = (file()