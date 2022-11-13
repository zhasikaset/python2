import numpy as np

given_arr = np.array([[1,2,3,6],[4,5,6,15],[7,8,9,24],[12,15,18,45]])

check_arr1 = np.array([[2,2,3,6],[4,5,6,15],[7,8,9,24],[12,15,18,45]])

check_arr2 = np.array([[1, 2, 3, 7 ],[4, 5, 6, 15],[7, 8, 9, 24],[12,15,18,45]])

check_arr3 = np.array([[1, 2, 3, 6 ],[4, 5, 6, 15],[7, 8, 9, 24],[12,15,18,46]])

def check(check_arr):

    dim = check_arr.shape[0]

    arr = check_arr.T

    position = [None,None]

    for i in range(dim):

        summ1 = sum(check_arr[i][0:-1])
    
        summ2 = sum(arr[i][0:-1])

        if summ1!=check_arr[i][-1]:

            position[0] = i
        
        if summ2!=arr[i][-1]:

            position[1] = i

    if position[0]!=None and position[1]!=None:

        summ = sum(check_arr[position[0]][0:-1])
        
        valid = summ-check_arr[position[0]][-1]+(check_arr[position[0]][position[1]])
        
        return "Wrong number: "+str(check_arr[position[0]][position[1]])+"\nShould equal: "+str(valid)

    else:
        
        return "Valid matrix"

print(check(check_arr2))