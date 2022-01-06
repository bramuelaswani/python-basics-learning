#create file
from shellmethods import shutil
def main():
    f=open('textfile.txt','w+')
for i in range(10):
    f.write('this is line' + str(i)+'\r\n')
    f.close()
    
#append file
#f=open("textfile.txt","a")
 #read
#f=open("textfile.txt","r")
#if f.mode=="r":
  #  contents=f.read()
    #print(contents)

if __name__=="_main_":
    main()
    