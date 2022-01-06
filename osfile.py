
import os
from os import path
import time

#print(os.name)
print("item exists:" + str(path.exists("textfile.txt")))
print("item is a file:"+str(path.isfile("textfile.txt")))
print("item is a directoory:"+str(path.isdir("textfile.txt")))
print("item is path:"+ str(path.realpath("textfile.txt")))
#get modification time
t=time.ctime(path.getmtime("textfile.txt"))
print(t)