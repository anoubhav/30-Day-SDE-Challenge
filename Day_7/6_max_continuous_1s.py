def findMaxConsecutiveOnes(nums):
    ans = msf = 0
    for num in nums:
        msf = msf + 1 if num else 0
        ans = max(ans, msf)
    return ans