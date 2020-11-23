def inbuilt(matrix):
    matrix[:] = list(map(list, zip(*matrix[::-1])))
    return matrix

def topdown_transpose(matrix):
    matrix[:] = matrix[::-1] # reverse the row order - topdown

    # Perform transposal: swap (i, j) with (j, i)
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

from copy import deepcopy
print(inbuilt(deepcopy(matrix)))
print(topdown_transpose(deepcopy(matrix)))


