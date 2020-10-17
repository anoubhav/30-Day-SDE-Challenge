def minDistance(word1, word2) -> int:
    # O(N^2) time and space
    n, m = len(word1), len(word2)
    dp = [[0]*(m+1) for _ in range(n+1)]
    
    for i in range(m+1):
        dp[0][i] = i
    for i in range(n+1):
        dp[i][0] = i
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                insert = dp[i-1][j] + 1
                delete = dp[i][j - 1] + 1
                replace = dp[i-1][j-1] + 1
                
                dp[i][j] = min(insert, delete, replace)

    return dp[n][m]

def minDistance1DP(s, t):
    # O(N^2) time and O(N) space
    n, m = len(s), len(t)

    prevrow = [0] * (m + 1)
    for j in range(m + 1):
        prevrow[j] = j
    
    for i in range(1, n + 1):
        current = [0] * (m + 1)
        current[0] = i

        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                current[j] = prevrow[j - 1]
            else:
                current[j] = min(prevrow[j - 1], current[j - 1], prevrow[j]) + 1
        
        prevrow = current[:]
    
    return prevrow[m]







        








word1 = "zoologicoarchaeologist"
word2 = "zoogeologist"

print(minDistance(word1, word2))