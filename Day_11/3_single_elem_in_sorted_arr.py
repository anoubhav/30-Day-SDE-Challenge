# Q: https://leetcode.com/problems/single-element-in-a-sorted-array/
def usingXOR(arr):
    # Time complexity: O(N). Space: O(1)
    ans = 0
    for i in arr:
        ans ^= i
    return ans

def usingBS(arr):
    # Time complexity: O(log N). Space: O(1)
    n = len(arr)
    lo, hi = 0, n - 1

    while lo <= hi:
        mid = (lo + hi)//2
        elem = arr[mid]
        if mid > 0 and arr[mid - 1] == elem:
            if mid%2 == 0:
                hi = mid - 1
            else:
                lo = mid + 1
        
        elif mid < n - 1 and arr[mid + 1] == elem:
            if mid%2 == 0:
                lo = mid + 1
            else:
                hi = mid - 1
        else:
            return elem
    return -1

# Ref: https://leetcode.com/problems/single-element-in-a-sorted-array/discuss/628036/Python-Binary-Search-O(logn)-explained
# https://leetcode.com/problems/single-element-in-a-sorted-array/discuss/100732/Short-compare-numsi-with-numsi1
def shorterBS(arr):
	lo, hi = 0, len(arr) - 1
	while lo < hi:
		mid = 2 * ((lo + hi) // 4) # to ensure mid is always even
		if arr[mid] == arr[mid+1]:
			lo = mid+2
		else:
			hi = mid
	return arr[lo]

# arr = [1,1,2,3,3,4,4,8,8]
arr = [3,3,7,7,10,11,11]
print(usingXOR(arr))
print(usingBS(arr))
print(shorterBS(arr))