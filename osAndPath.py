import os
from os import path
import datetime
from datetime import date, time, timedelta
import time
#working with os path module
def main():
    print(os.name)

    print("item exists:" +str(path.exists("textfile.txt")))
    print("item is a file:" + str(path.isfile("textfile.txt")))
    print("item is directory:" +str(path.isdir("textfile.txt")))   

#working with file path
    print("item path:"+ str(path.realpath("textfile.txt")))
    print("item path and name:"+ str(path.realpath("textfile.txt")))

#get the modification time
t=time.ctime(path.getmtime("textfile.txt"))
print(t)
print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))
td=datetime.datetime.now()-datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
print("it has been "+ str(td) + "since the file was modified")
print("or,"+ str(td.total_seconds())+"seconds")

if __name__=="__main__": 
    main()
