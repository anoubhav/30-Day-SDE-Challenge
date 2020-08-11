def extraSpace(matrix):
    # Time: O(m*n). Space O(m + n) using two sets.
    n, m = len(matrix), len(matrix[0])
    row, col = set(), set()
    for r in range(n):
        for c in range(m):
            if matrix[r][c] == 0:
                row.add(r)
                col.add(c)

    ## Set the rows and columns to zeros (the way I did it; A lot of elements are set to 0 more than once.)
    # for r in row:
    #     for i in range(m):
    #         matrix[r][i] = 0

    # for c in col:
    #     for r in range(len(matrix)):
    #         matrix[r][c] = 0

    ## Set the rows and columns to zeros (LC editorial)
    for r in range(n):
        for c in range(m):
            if r in row or c in col:
                matrix[r][c] = 0

    return matrix

# Ref: https://leetcode.com/problems/set-matrix-zeroes/solution/
def BruteNoSpace(matrix):
    # Time: O(M*N * (M + N)) and Space: O(1)
    # Two - pass
    n, m = len(matrix), len(matrix[0])
    MODIFIED = -10**6 # A large dummy value; out of the possible range of input.
    for r in range(n):
        for c in range(m):
            if matrix[r][c] == 0:
                for col in range(m):
                    matrix[r][col] = MODIFIED if matrix[r][col]!=0 else 0
                for row in range(n):
                    matrix[row][c] = MODIFIED if matrix[row][c]!=0 else 0
    
    # Make a second pass and change all MODIFIED elements to 0
    for r in range(n):
        for c in range(m):
            if matrix[r][c] == MODIFIED:
                matrix[r][c] = 0

    return matrix

# Ref: https://leetcode.com/problems/set-matrix-zeroes/solution/
def OptimalNoSpace(matrix):
    # Time : O(M*N) and Space: O(1)
    n, m = len(matrix), len(matrix[0]) 

    # Since first cell for both first row and first column is the same i.e. matrix[0][0]. We can use an additional variable for either the first row/column.            
    first_col = False
    for r in range(n):
        if matrix[r][0] == 0:
            first_col = True
        
        for c in range(1, m):
            if matrix[r][c] == 0:
                matrix[r][0] = 0
                matrix[0][c] = 0
    
    # Set the rows and columns to zero (not including the first one)
    for r in range(1, n):
        for c in range(1, m):
            if not matrix[r][0] or not matrix[0][c]:
                matrix[r][c] = 0
    
    # Set the first row to 0
    if matrix[0][0] == 0:
        for c in range(m):
            matrix[0][c] = 0
    
    # Set the first column to 0
    if first_col:
        for r in range(n):
            matrix[r][0] = 0
    
    return matrix
            
matrix = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]

from copy import deepcopy
print(extraSpace(deepcopy(matrix)))
print(BruteNoSpace(deepcopy(matrix)))
print(OptimalNoSpace(matrix))


# Main difference between BruteNoSpace and OptimalNoSpace:
# The inefficiency in the second approach (Brute) is that we might be repeatedly setting a row or column even if it was set to zero already.

#  We can avoid this by postponing the step of setting a row or a column to zeroes.

# (Optimal) We can rather use the first cell of every row and column as a flag. This flag would determine whether a row or column has been set to zero. This means for every cell instead of going to M+N cells and setting it to zero we just set the flag in two cells.