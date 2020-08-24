# Worst case example: 'a'*n
# Q: https://leetcode.com/problems/palindrome-partitioning/

def partitionDFS(s):
    # Time complexity: O(2^n) where n is the length of the s. nC0 + nC1 + nC2.. + nCn = 2^n.
    # Space complexity: O(n).
    ans = []

    n = len(s)
    def isPal(s):
        # return s == s[::-1]
        b, e = 0, len(s) - 1
        while b < e:
            if s[b] != s[e]: return False
            b += 1
            e -= 1
        return True

    def recurse(parti, ind, n):
        if ind == n:
            ans.append(parti.copy())
        else:
            i = ind
            while i < n:
                curr = s[ind: i + 1]

                if isPal(curr):
                    recurse(parti + [curr], i + 1, n)
                
                i += 1

    recurse([], 0, n)
    return ans

# Below solutions were found from discussions tab. They have the same worst case time complexity as mine of O(2^n)

# Ref: https://leetcode.com/problems/palindrome-partitioning/discuss/42025/1-liner-Python-Ruby
def oneLiner(s):
    return [s[i:] + rest 
            for i in range(1, len(s) + 1) 
            if s[:i] == s[:i][::-1]
            for rest in oneLiner(s[i:])] or [[]]

# Ref: https://leetcode.com/problems/palindrome-partitioning/discuss/315175/python-dp-bottom-up-beats-99.55
def partitionDP(s):
    dp = [[] for _ in range(len(s) + 1)]
    # Let dp[i] store the list of palindromes in s[i:]. dp[-1] is the number of palindromes in s[len(s):] is an empty list of lists.
    dp[-1] = [[]]

    # dp[i: end] = dp[i: j] + dp[j: end] for all j's where i < j <= len(s) given dp[i: j] is a palindrome

    # Iterate from suffix side
    for i in range(len(s) - 1, -1, -1):
        for j in range(i + 1, len(s) + 1):
            if s[i:j] == s[i:j][::-1]:
                for each in dp[j]:
                    dp[i].append([s[i:j]] + each)
    return dp[0]

s = "aab"
print(partition(s))
