from datetime import date
from datetime import time
from datetime import timedelta
from datetime import datetime
def main():
    today=date.today()
    print(today)
    print('date components:'+ today.time, today.month, today.year)
    print(today.weekday())
 #date objects
now=datetime.now()
print(now)
t=datetime.time(localtime.now())
print(t)
print(datetime.now().strftime('%a, %d, %B, %y')) #learn more about strftime formatting features
print(timedelta(days=365,hours=5, minutes=1) #time delta objects
#print(str(now+str(timedelta(days=365)))
if __name__=="__main_":
    main()

print(date.today())


'''def main():
    leo = date.today()
    print(leo)
 
    
if __name__ == "" 
main()'''
    