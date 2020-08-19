def removeDuplicates(nums):
    # O(N) time complexity. O(1) space.
    n = len(nums)
    slow = 0
    for i in range(n):
        if i > 0 and nums[i]!=nums[i-1]:
            slow += 1
            nums[slow] = nums[i]
    return slow + 1