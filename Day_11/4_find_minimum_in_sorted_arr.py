# Q: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# NO DUPLICATES

# Ref: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/discuss/158940/Beat-100%3A-Very-Simple-(Python)-Very-Detailed-Explanation
def shorterBS(nums):
    lo, hi = 0, len(nums) - 1

    # The problem's invariant for shifted cases is left element always greater than right. Maintaining it is sufficient for binary search. And this invariant is NOT satisifed at the inflection point (our answer)

	# proof for loop termination:
    #     lo < hi then lo + hi < 2hi
    #     and mid = (lo + hi) /2  < 2hi/2
	# So mid < hi 

    # after each iteration either the 'high' decreases or the 'low' increases, so the interval [low, high] will always shrink.

    while lo < hi:
        mid = (lo + hi)//2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    return nums[lo]




# ref: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/solution/ ; Also errichto's binary search video
def usingBS(nums):
    # Time: O(log N). Space: O(1)
    n = len(nums)
    if n == 0: return None
    elif n == 1: return nums[0]
    
    if nums[0] < nums[-1]:
        return nums[0]
    
    lo, hi = 0, n - 1
    first = nums[0]
    
    while lo <= hi:
        mid = (lo + hi)//2
        
        if nums[mid + 1] < nums[mid]:
            return nums[mid + 1]
        
        if nums[mid] < nums[mid - 1]:
            return nums[mid]
        
        if first < nums[mid]:
            lo = mid + 1
        else:
            hi = mid
            
    return nums[mid]

