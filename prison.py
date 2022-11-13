import numpy as np

# As I understand that if 0th cell (our cell) is 1 so we can leave eat but it will switch position of other cells and we also counted as freed 

greed1 = np.array([1, 1, 0, 0, 0, 1, 0])

greed2 = np.array([1, 1, 1]) 

greed3 = np.array([1, 0, 0]) 

greed4 = np.array([0, 1, 1, 1]) 

greed5 = np.array([1, 0, 1, 0]) 

def change(greed):

    length = greed.shape[0]

    for i in range(length):

        greed[i] = (greed[i]+1)%2

    return greed

def how_many(greed):

    if greed[0] == 0:
        
        return 0

    else:

        length = greed.shape[0]

        greed = change(greed)

        pos, freed = 1, 1 

        while pos < length:

            if greed[pos] == 1:

                freed+=1

                greed = change(greed)

                pos+=1

            else:

                pos+=1

        return freed

print(how_many(greed1))

print(how_many(greed2))

print(how_many(greed3))

print(how_many(greed4))

print(how_many(greed5))
