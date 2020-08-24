# Q: https://leetcode.com/problems/search-in-rotated-sorted-array/

from bisect import bisect_left
def usingTwoPassBS(nums, target):
    # 1) Find the pivot/inflection point by binary search
    # 2) binary search either on the left side of right side of pivot.

    # Time complexity: O (log N). Space: O(1)

    # empty array
    if not nums: return -1

    # Step 1: find pivot; constraints: all numbers are unique

    # Ascending order array; search for element directly; there is no rotation
    if nums[0] < nums[-1]:
        ind = bisect_left(a = nums, x = target)
    else:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi)//2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid

        # find the pivot
        pivot = lo

        if target < nums[0]:
            lo, hi = pivot, len(nums)
        else:
            lo, hi = 0, pivot

        ind = bisect_left(a = nums, x = target, lo = lo, hi = hi)

    return ind if (ind < len(nums) and nums[ind] == target) else -1


nums = [1, 3]
target = 3

print(usingTwoPassBS(nums, target))


    