import random

n = random.randint(0,7)

datalist = [1452, 11.23, 1+2j, True, 'student', (0, -1), [5,12], {"class":'V', "section":'A'}]

print(datalist[n],type(datalist[n]))