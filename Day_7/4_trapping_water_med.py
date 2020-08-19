# Problem: https://leetcode.com/problems/container-with-most-water/
def brute(height):
    # O(N^2) time. Space O(1)
    n = len(height)
    maxa = 0
    for i in range(n):
        for j in range(i + 1, n):
            maxa = max(maxa, min(height[i], height[j])*(j - i))
    return maxa

def twoPointer(height):
    # O(N) time complexity. Space O(1)
    n = len(height)
    l, r = 0, n - 1
    maxa = min(height[l], height[r])*(r - l)
    while l < r:
        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1
        maxa = max(maxa, min(height[l], height[r])*(r - l))
    return maxa


# From editorial
# Initially we consider the area constituting the exterior most lines. Now, to maximize the area, we need to consider the area between the lines of larger lengths. If we try to move the pointer at the longer line inwards, we won't gain any increase in area, since it is limited by the shorter line. But moving the shorter line's pointer could turn out to be beneficial, as per the same argument, despite the reduction in the width. This is done since a relatively longer line obtained by moving the shorter line's pointer might overcome the reduction in area caused by the width reduction.