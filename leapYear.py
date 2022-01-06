def is_leap(year):
    # Write your logic here
    #year>=1990 and year<=10**5
        if year>=1900 and year<=10**5:
            if ((year%4) == 0):
                if (year%100 == 0):
                    if (year%400 == 0):
                        return True
                    else:
                        return False
                else:
                    return True
            else:
                return False    
        else:
            return False
    
         

year = int(input())
print(is_leap(year))