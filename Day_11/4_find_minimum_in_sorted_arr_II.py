# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

# DUPLICATES ALLOWED

def usingBS(nums):
    # Time complexity: O(N). if array has n same numbers the else condition will be executed. This is optimal solution.
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi)//2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        elif nums[mid] < nums[hi]:
            hi = mid
        else:
            if nums[hi - 1] > nums[hi]:
                # breaks out on first instance. 
                lo = hi
                break
            # only this modification is required for duplicates
            hi -= 1    
    return nums[lo]