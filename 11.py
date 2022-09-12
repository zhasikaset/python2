zodiacs = {0:"Rat",1:"Ox",2:"Tiger",3:"Hare",4:"Dragon",5:"Snake",6:"Horse",7:"Ram",8:"Monkey",9:"Rooster",10:"Dog",11:"Pig"}
n = int(input("Input your birth year: "))
print("Your Zodiac sign is : {}".format(zodiacs[(n-1900)%12]))
