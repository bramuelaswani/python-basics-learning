from genericpath import exists
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import  ZipFile
import zipfile

def main():
#make a duplicate of an existing file
# if path.exists("textfile.txt"):
    src=path.realpath("textfile.txt")
    #make a copy
    dst=src +".bak"
    #copy over the permission
    shutil.copy(src, dst)
    shutil.copy.stat(src, dst)

    #rename the originsl file
    #os.rename("textfile.txt","newfile.txt")

    #now put the things into a zip archive
    root_dir, tail=path.split(src)
    shutil.make_archive("archive","zip", root_dir)
    with zipfile("testzip.zip","w") as newzip:
         newzip.write("textfile.txt")
if __name__=="_main_":
    main()

