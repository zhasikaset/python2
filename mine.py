import numpy as np

grid1 = np.array([["-", "-", "-", "-", "-"],
                  ["-", "-", "-", "-", "-"],
                  ["-", "-", "#", "-", "-"],
                  ["-", "-", "-", "-", "-"],
                  ["-", "-", "-", "-", "-"]])

grid2 = np.array([["-", "-", "-", "-", "#"],
                  ["-", "-", "-", "-", "-"],
                  ["-", "-", "#", "-", "-"],
                  ["-", "-", "-", "-", "-"],
                  ["#", "-", "-", "-", "-"]])

grid3 = np.array([["-", "-", "-", "#", "#"],
                  ["-", "#", "-", "-", "-"],
                  ["-", "-", "#", "-", "-"],
                  ["-", "#", "#", "-", "-"],
                  ["-", "-", "-", "-", "-"]]) 

def mp(grid):
    
    dim = grid.shape
    
    zeros = np.array([['0' for i in range(dim[1]+2)] for j in range(dim[0]+2)])
    
    coordinates = np.argwhere(grid == "#")
    
    for i in coordinates:
    
        zeros[i[0]+2][i[1]+1] = str(int(zeros[i[0]+2][i[1]+1])+1)
    
        zeros[i[0]+2][i[1]] = str(int(zeros[i[0]+2][i[1]])+1)
    
        zeros[i[0]+2][i[1]+2] = str(int(zeros[i[0]+2][i[1]+2])+1)
    
        zeros[i[0]+1][i[1]+0] = str(int(zeros[i[0]+1][i[1]])+1)
    
        zeros[i[0]][i[1]] = str(int(zeros[i[0]][i[1]])+1)
    
        zeros[i[0]][i[1]+1] = str(int(zeros[i[0]][i[1]+1])+1)
    
        zeros[i[0]][i[1]+2] = str(int(zeros[i[0]][i[1]+2])+1)
    
        zeros[i[0]+1][i[1]+2] = str(int(zeros[i[0]+1][i[1]+2])+1)
    
    for i in coordinates:
    
        zeros[i[0]+1][i[1]+1] = '#'
    
    zeros = zeros[1:-1]
    
    output = np.array([])
    
    for rows in zeros:
    
        output = np.append(output,rows[1:-1])
    
    output = output.reshape(dim[0],dim[1])
    
    return output

print(mp(grid1))

print(mp(grid2))

print(mp(grid3))