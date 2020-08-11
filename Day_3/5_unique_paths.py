def uniquePathsDP(m, n):
    # O(m*n) time and space.
    dp = [[1]*(m) for _ in range(n)]

    for r in range(1, n):
        for c in range(1, m):
            dp[r][c] = dp[r-1][c] + dp[r][c-1]
    
    return dp[-1][-1]

def uniquePathsOptimised(m, n):
    # O(m*n) time. O(n) space.
    if n > m:
        n, m = m, n

    dp = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] = dp[j - 1] + dp[j]  # left + top
    return dp[-1]

# Ref: https://leetcode.com/problems/unique-paths/discuss/22958/Math-solution-O(1)-space
def uniquePathsCombinatorics(m, n):
    # Time complexity: O(N). Space complexity: O(1)

    # math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1)

    if m == 1 or n == 1: return 1
    m -= 1
    n -= 1
    if m < n:
        m, n = n, m
    
    ans = 1
    j = 1
    for num in range(m+1, m + n + 1):
        ans *= num
        ans /= j
        j += 1
    return int(ans)


grid = (100, 100)
print(uniquePathsDP(*grid))
print(uniquePathsCombinatorics(*grid))
print(uniquePathsOptimised(*grid))