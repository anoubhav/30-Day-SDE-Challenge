def generatePascal(n):
    # O(N^2) time complexity. Space complexity: O(N^2). Uses the symmetric nature of Pascal triangle.
    if n == 0: return []
    if n == 1: return [[1]]

    ans = [[1], [1, 1]]
    for sz in range(3, n+1):
        t = [0]*sz

        fill = (sz + 1)//2
        t[0] = t[sz - 1] = 1

        prev = ans[-1]
        for i in range(fill):
            elem = sum(prev[i:i + 2])
            t[i + 1] = t[sz - 1 - (i + 1)] = elem
        
        ans.append(t)
    return ans

# Ref: https://leetcode.com/problems/pascals-triangle/discuss/38128/Python-4-lines-short-solution-using-map.
def OffsetSum(n):
    # explanation: Any row can be constructed using the offset sum of the previous row. Example:

    #     1 3 3 1 0 
    #  +  0 1 3 3 1
    #  =  1 4 6 4 1

    if n == 0: return []
    ans = [[1]]
    for _ in range(1, n):
        ans.append(list(map(lambda x, y: x + y, [0] + ans[-1], ans[-1] + [0])))
    return ans

def DP(n):
    ans = [[1]*(i + 1) for i in range(n)]
    for i in range(2, n):
        for j in range(1, i):
            ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
    return ans
    
n = 0
print(generatePascal(n))
print(OffsetSum(n))
print(DP(n))
