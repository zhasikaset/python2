import numpy as np

seats1 = np.array([[1, 2, 3, 2, 1, 1],[2, 4, 4, 3, 2, 2],[5, 5, 5, 5, 4, 4],[6, 6, 7, 6, 5, 5]])

seats2 = np.array([[2, 0, 0], [1, 1, 1], [2, 2, 2]])

def check(arr):

    dim = arr.shape

    for j in range(dim[1]):

        columns = []

        for i in range(dim[0]):
            
            columns.append(arr[i][j])

        for k in range(len(columns)-1):

            if columns[k]>columns[k+1]:
            
                return False

    return True

print(check(seats1))

print(check(seats2))