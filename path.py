import numpy as np

from math import *

path1 = [("00000"),("01006"),("02000"),("30050"),("00004")] 

path2 = [("001"),("002"),("003")] 

path3 = [("00020000"),("01000000")]

path4 = [("01234"),("00000"),("50000")]

def shortest(arr):

    nump = np.array([])

    for i in arr:

        for j in i:

            nump = np.append(nump,j)

    nump = nump.reshape(len(arr),int(len(nump)/len(arr)))

    summ = 0

    for rows in nump:

        for elem in rows:

            summ+=int(elem)

    maxi = int(((1+8*summ)**(1/2)-1)/2)

    coordinates = np.array([])

    for i in range(1,maxi+1):

        coor = np.argwhere(nump == str(i))

        coordinates = np.append(coordinates,[str(i),coor[0]])

    a = (len(coordinates))

    coordinates = coordinates.reshape(int(a/2),2)

    path_len = 0

    for i in range(maxi-1):

        diff = np.subtract(coordinates[i][1],coordinates[i+1][1])

        path_len+=abs(diff[0])+abs(diff[1])

    return path_len

print(shortest(path1))

print(shortest(path2))

print(shortest(path3))

print(shortest(path4))