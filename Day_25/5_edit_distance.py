def minDistance(word1, word2) -> int:
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

word1 = "zoologicoarchaeologist"
word2 = "zoogeologist"

print(minDistance(word1, word2))