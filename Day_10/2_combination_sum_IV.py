# Disclaimer: This is not a backtracking problem
# Q: https://leetcode.com/problems/combination-sum-iv/

def DP(nums, target):
    # Time and space complexity: O(N*M), where N = len(nums) and M = len(target). 
    
    dp = [0]*(target + 1)
    # by setting this to one, dp[num] for every num in nums will become 1 in the below loop.
    dp[0] = 1  
    # helps in breaking early
    nums.sort()
            
    for i in range(target + 1):
        for num in nums:
            if i + num < target + 1:
                dp[i + num] += dp[i]
            else: break
    return dp[target]