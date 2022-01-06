from os import path
import shutil
from shutil import make_archive
if path.exists("textfile.txt"):
    src=path.realpath("textfile.txt")
    #back upi
    dst=src+".bak"
    #copy
    shutil.copy(src,dst)
    shutil.copystat(src,dst)
    #rename
    #os.rename("textfile.txt", "newfile.txt")
    root_dir,tail=path.split(src)
    shutil.make_archive("archive","zip",root_dir)