# Q: https://leetcode.com/problems/merge-sorted-array/
# It is different then SDE sheet. Refer to GFG for intended solution.

# GFG: https://www.geeksforgeeks.org/merge-two-sorted-arrays-o1-extra-space/#:~:text=We%20are%20given%20two%20sorted,allowed%20in%20O(1).


# fill backwards.
def merge(nums1, m, nums2, n):
    # Time complexity: O(m + n). Space O(1)
    while m > 0 and n > 0:
        if nums1[m-1] >= nums2[n-1]:
            nums1[m + n - 1] = nums1[m-1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n-1]
            n -= 1
    if n > 0:
        nums1[:n] = nums2[:n]