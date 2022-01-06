def gradingSystem(score):
    if score>90 and score<100:
       return 'A'
    elif score>= 80 and score<=90:
        return'A-'
    elif score>=70 and score<=80:
        return 'B+'
    elif score>=60 and score <=70:
        return 'B'
    elif score>= 50 and score<=60:
        return 'C'
    elif score>= 40 and score<=50:
        return 'D'
    else: 
        return 'E'
count=0
while count< 11:
    score= int(input('enter number'))
    val=gradingSystem(score)
    print(val)
    count+=1
    
