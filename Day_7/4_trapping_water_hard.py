# Problem: https://leetcode.com/problems/trapping-rain-water/
def bruteForce(height):
    # Time complexity: O(N^2). Space complexity: O(1)

    # For each element in the array, we find the maximum level of water it can trap after the rain, which is equal to the minimum of maximum height of bars on both the sides minus its own height.

    # You are adding the vertical columns at each i.

    ans = 0
    n = len(height)
    # Iterate over all elements in array
    for i in range(n):
        lmax = rmax = height[i]
        l, r = i, i
        # O(N) for each element in array.
        while l > 0: 
            l -= 1
            lmax = max(lmax, height[l])
            
        while r < n-1:
            r += 1
            rmax = max(rmax, height[r])
            
        ans += min(lmax, rmax) - height[i]
    return ans

def OptimisedBruteForce(height):
    # This is a dynamic programming solution
    # Time complexity: O(N). Space complexity: O(N)
    ans = 0
    n = len(height)
    lmax, rmax = [0]*n, [0]*n
    # Precompute lmax and rmax for each position in array in O(N) time and space.
    for i in range(n):
        if i > 0:
            lmax[i] = max(lmax[i-1], height[i])
            rmax[n - i - 1] = max(rmax[n - i], height[n - i - 1])
        else:
            lmax[0] = height[0]
            rmax[n-1] = height[n-1]

    # Iterate over all elements of array
    for i in range(n):
        ans += min(lmax[i], rmax[i]) - height[i]
    
    return ans

# Ref: https://leetcode.com/problems/trapping-rain-water/solution/
def twoPointer(height):
    # O(N) time and O(1) space.

    n = len(height)
    l, r, lmax, rmax, ans = 0, n-1, 0, 0, 0
    while l < r:
        if height[l] > lmax: lmax = height[l]
        if height[r] > rmax: rmax = height[r]
        if lmax > rmax:
            ans += rmax - height[r]
            r -= 1
        else:
            ans += lmax - height[l]
            l += 1
    return ans