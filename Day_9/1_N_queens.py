# Q: https://leetcode.com/problems/n-queens/ - configurations
# Q: https://leetcode.com/problems/n-queens-ii/submissions/ - number of configurations.


# Time complexity: O(N!), think rooks (https://stackoverflow.com/a/56959609)
# Space complexity: O(N!) recursion stack.
def solveNQueens(n):
    count = 0 # number of distinct configurations
    ans = [] # list of configurations
    columns, diagL, diagR = set(), set(), set()
    board = [["."]*n for _ in range(n)]

    def solve(row, board):
        nonlocal count
        if row == n + 1:
            count += 1

            config = []
            for r in board:
                config.append(''.join(r))
            
            ans.append(config)
        
        else:
            for col in range(1, n + 1):
                # Think of slopes y = m*x + b. m = +- 1
                if col in columns or (row + col) in diagL or (row - col) in diagR: continue
                
                columns.add(col), diagL.add(row + col), diagR.add(row - col)
                
                board[row - 1][col - 1] = 'Q'
                solve(row + 1, board)
                board[row - 1][col - 1] = '.'

                columns.remove(col), diagL.remove(row + col), diagR.remove(row - col)

    solve(1, board)
    print('Number of distinct configurations: ', count)
    return ans

print(solveNQueens(4))
