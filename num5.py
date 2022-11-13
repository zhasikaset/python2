import numpy as np

password = "HeLen-eda"

def shift(c):
    
    place = (ord(c)-ord('a')+1)%(26)+ord('a')
    
    return chr(place)

def deshift(c):

    place = (ord(c)-ord('a')-1)%(26)+ord('a')

    return chr(place)

def isit(string):

    cnt = 0

    for i in string:

        if i not in "abcdefghijklmnopqrstuvwxyz":

            cnt+=1

    return cnt

def check(password):
    
    if len(password)!=9 or isit(password)!=0:

        return "Bang,Bang,Bang!"

    else:

        part1 = password[0:3]

        part2 = password[3:6]

        part3 = password[6:9]

        part1 = str(ord(part1[0])-ord('a')+1)+part1[1]+str(ord(part1[2])-ord('a')+1)

        part2 = part2[::-1]

        part3 = shift(part3[0])+shift(part3[1])+shift(part3[2])

        return part2+part3+part1

def decode(password):

    part1 = password[6:]

    part2 = password[0:3]

    part3 = password[3:6]

    part2 = part2[::-1]

    part3 = deshift(part3[0])+deshift(part3[1])+deshift(part3[2])

    c1,c2 = "",""

    i = 0

    while part1[i] not in "abcdefghijklmnopqrstuvwxyz":

        c1+=part1[i]

        i+=1

    c2 = part1[i]

    c3 = part1[i+1:]
   
    part1 = chr(int(c1)-1+ord('a'))+c2+chr(int(c3)-1+ord('a'))
 
    return part1+part2+part3    

print(check(password))

print(decode("hsajsi13u2"))
