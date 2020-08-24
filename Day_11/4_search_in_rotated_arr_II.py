# Q: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
# Allows for DUPLICATES

from bisect import bisect_left
def usingBS(nums, target):
    # Time: O(N). Space: O(1)
    if not nums: return False
    
    if nums[0] < nums[-1]:
        ind = bisect_left(a = nums, x = target)
    else:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi)//2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            elif nums[mid] < nums[hi]:
                hi = mid
            else:
                # This makes it O(N)
                if nums[hi - 1] > nums[hi]:
                    lo = hi
                    break
                hi -= 1

        # find the pivot
        pivot = lo

        if target < nums[0]:
            lo, hi = pivot, len(nums)
        else:
            lo, hi = 0, pivot

        ind = bisect_left(a = nums, x = target, lo = lo, hi = hi)

    return (ind < len(nums) and nums[ind] == target)