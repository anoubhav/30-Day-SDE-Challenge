# Time complexity: O(N ^ M) where n is the number of possibilities for each square (i.e., 9 in classic Sudoku) and m is the number of spaces that are blank.

# Space complexity: O(N ^ M) recursion stack
def solveSudokuMine(board):
    # 300ms
    def solve(row, cc):
        if row == 10:
            return True
        else:
            if board[row-1][cc-1] == '.':

                # Find the column
                column = [board[i - 1][cc - 1] for i in range(1, 10)]

                # Find the box. lc: left corner of the box
                lc = (3 * ((row - 1)//3) , 3 * ((cc - 1)//3))
                box = set()
                for r in range(lc[0], lc[0] + 3):
                    for c in range(lc[1], lc[1] + 3):
                        if board[r][c]!='.': box.add(board[r][c])

                # Fill board[row-1][cc-1] and move onto the next sudoku element
                for num in range(1, 10):
                    char = str(num)
                    if char in board[row - 1] or char in column or char in box: continue

                    board[row - 1][cc - 1] = char
                    box.add(char)
                    column[row - 1] = char
                    
                    # move to next row
                    if cc == 9:
                        t = solve(row + 1, 1)
                    # move to next column
                    else:
                        t = solve(row, cc + 1)
                    
                    # backtrack if solution not found
                    if not t:
                        board[row - 1][cc - 1] = '.'
                        box.remove(char)
                        column[row - 1] = '.'
                    else:
                        return True
            else:
                if cc == 9:
                    t = solve(row + 1, 1)
                else:
                    t = solve(row, cc + 1)
                if t:
                    return True
    solve(1, 1)

# Faster implementations. Ref: https://leetcode.com/problems/sudoku-solver/discuss/140837/Python-very-simple-backtracking-solution-using-dictionaries-and-queue-~100-ms-beats-~90

def solveSudoku(board):
    # 100ms
    import collections
    rows, cols, triples, visit = collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set), collections.deque([])
    for r in range(9):
        for c in range(9):
            if board[r][c] != ".":
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                triples[(r // 3, c // 3)].add(board[r][c])
            else:
                visit.append((r, c))
    def dfs():
        # visited deque is empty
        if not visit:
            return True
        r, c = visit[0]
        t = (r // 3, c // 3)
        for dig in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}:
            if dig not in rows[r] and dig not in cols[c] and dig not in triples[t]:
                board[r][c] = dig
                rows[r].add(dig)
                cols[c].add(dig)
                triples[t].add(dig)
                visit.popleft()
                if dfs():
                    return True
                else:
                    board[r][c] = "."
                    rows[r].discard(dig)
                    cols[c].discard(dig)
                    triples[t].discard(dig)
                    visit.appendleft((r, c))
        return False
    dfs()

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

# solveSudokuMine(board)
solveSudoku(board)


# for row in board:
#     print(*row)
