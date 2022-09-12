m = int(input("INPUT THE MONTH :  "))
d = int(input("INPUT THE DAY : "))
def toseason(m,d):
    month = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
    if m==2 and d>=30:
        print("That is impossible,enter correct data")
    else:
        if m==12 or m==1 or m==2:
            print("{}, {}. Season is {}. ".format(month[m],d,"winter"))
        elif m==3 or m==5 or m==4:
            print("{}, {}. Season is {}. ".format(month[m],d,"spring"))
        elif m==6 or m==7 or m==8:
            print("{}, {}. Season is {}. ".format(month[m],d,"summer"))
        else:
            print("{}, {}. Season is {}. ".format(month[m],d,"autumn"))
toseason(m,d)
            


