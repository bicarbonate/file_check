import glob
import os
from datetime import datetime


monitor_files = []

dirnames = "adr01 chpt emb01 exp01 iix01ii".split()

def monitor(name):
  os.chdir("/home/skeer/Documents/Projects/Python_temp/home/"+name+"/upload/")
  for file in glob.glob("*.pgp"):
    if os.path.isfile(file):
      last_modified_date = datetime.fromtimestamp(os.path.getmtime(file))
    else:
      last_modified_date = datetime.fromtimestamp(0)
  monitor_files.append(
    "{name} | {file} | {last_modified_date}\n".format(
      name=name,
      file=file,
      last_modified_date=last_modified_date)

for name in dirnames:
  monitor(name)
print("\n".join(monitor_files))
