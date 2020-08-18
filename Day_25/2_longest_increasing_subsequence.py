# Ref: https://leetcode.com/problems/longest-increasing-subsequence/solution/
def topDown(nums):
    # O(n * n) time and space
    n = len(nums)
    dp = [[-1]*(n+1) for _ in range(n)]

    def recurse(nums, prev_ind, curr_ind, dp):
        if curr_ind == len(nums): return 0

        elif dp[prev_ind + 1][curr_ind] < 0:
            taken = 0
            if prev_ind < 0 or nums[prev_ind] < nums[curr_ind]:
                taken = 1 + recurse(nums, curr_ind, curr_ind + 1, dp)
            
            nottaken = recurse(nums, prev_ind, curr_ind + 1, dp)

            dp[prev_ind + 1][curr_ind] = max(taken, nottaken)

        return dp[prev_ind + 1][curr_ind]

    return recurse(nums, -1, 0, dp)

def BottomUp(nums):
    # Much faster than topDowna and usingLCS (> 5 times). Time complexity: O(n * n). Space: O(n)

    # dp[i] represents the length of the longest increasing subsequence possible considering the array elements upto the i th index only ,by necessarily including the ith element.

    n = len(nums)
    if n < 2: return n

    dp = [0]*n
    dp[0] = 1
    ans = 1
    for i in range(n):
        maxval = 0
        for j in range(i):
            if nums[j] < nums[i]:
                maxval = max(maxval, dp[j])
        dp[i] = maxval + 1
        ans = max(ans, dp[i])
    return ans

def usingLCS(nums):
    # Time complexity: O(m * n + n* log n + n) = O(m * n). Space: O(m * n). 

    # The longest increasing subsequence of a sequence S is the longest common subsequence of S and T, where T is the result of sorting S.
    
    if not nums: return 0
    # store sorted array.
    temp = sorted(nums)
    
    # remove duplicates.
    unique = [temp[0]]
    for i in temp[1:]:
        if i > unique[-1]:
            unique.append(i)
    
    # Find LCS between array and sorted array.
    n, m = len(nums), len(unique)
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if nums[i-1] == unique[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]


from bisect import bisect_left
def binarySearchConstruction(nums):
    last = [nums[0]]

    for i in nums[1:]:
        ind = bisect_left(last, i)
        if ind == len(last):
            last.append(i)
        else:
            last[ind] = i
    return len(last)

nums = [10,9,2,5,3,7,101,18]
print(usingLCS(nums))
print(topDown(nums))
print(BottomUp(nums))
print(binarySearchConstruction(nums))