def LCS_Bottom(s, t):
    # O(m * n) time and space.
    n, m = len(s), len(t)
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i-1] == t[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]

def LCS_Bottom_Optimised_Space(s, t):
    # O(m * n) time. O(n) space.
    n, m = len(s), len(t)
    if n > m: return LCS_Optimised(t, s)
    dp = [0]*(n + 1)
    for i in range(1, m + 1):
        prev = 0
        for j in range(1, n + 1):
            temp = dp[j]
            if t[i-1] == s[j - 1]:
                dp[j] = prev + 1
            else:
                dp[j] = max(dp[j], dp[j - 1])
            prev = temp
    return dp[n]

def LCS_TopDown(s, t):
    n, m = len(s), len(t)
    dp = [[-1] * (m + 1) for _ in range(n + 1)]

    def recurse(s, t, i, j, dp):
        if dp[i][j] < 0:
            if i == 0 or j == 0:
                return 0
            elif s[i-1] == t[j-1]:
                dp[i][j] = 1 + recurse(s, t, i - 1, j - 1, dp)
            else:
                dp[i][j] = max(recurse(s, t, i-1, j, dp), recurse(s, t, i, j-1, dp))
        return dp[i][j]
    
    recurse(s, t, n, m, dp)
    return dp[n][m]


s = "oxcpqrsvwf"
t = "shmtulqrypy"
print(LCS_Bottom('asdf', 'assd'))
print(LCS_Bottom('asdf', 'bbbbb'))
print(LCS_Bottom_Optimised_Space(s, t))
print(LCS_TopDown(s, t))
