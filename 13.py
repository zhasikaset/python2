import datetime

y = int(input("Input a year : "))

m = int(input("Input a month [1-12] : "))

d = int(input("Input a day [1-31] : "))

today = datetime.datetime(y,m,d)

next_day  = (today+datetime.timedelta(days=1)).strftime("%Y-%m-%d").split("-")

if next_day[1][0]=="0":
 
    next_day[1] = next_day[1][1]

if next_day[2][0]=="0":
    
    next_day[2] = next_day[2][1]

print("The next date is "+next_day[0]+"-"+next_day[1]+"-"+next_day[2])