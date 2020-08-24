# Q: https://www.interviewbit.com/problems/matrix-median/

def findMedianNaive(mat):
    # Time complexity: O(r * c * log (r * c)) for sorting. Space complexity: O(r * c)
    all_lst = []
    for row in mat:
        all_lst += row
    all_lst.sort()
    return all_lst[len(all_lst)//2]

# Ref: https://www.geeksforgeeks.org/find-median-row-wise-sorted-matrix/
from bisect import bisect_right
def findMedianBS(mat):
    # Time complexity: O(log (max num) * r * log c) ~ O(32 * r * log c) ~ O(r * log c). As the max num <= 10**9. Space complexity: O(1)

    r, c = len(mat), len(mat[0])
    mi, mx = 10**9, 0
    for i in range(r):
        mi = min(mi, mat[i][0])
        mx = max(mx, mat[i][-1])
    
    desired = (r * c + 1)//2

    lo, hi = mi, mx
    while lo <= hi:
        mid = (lo + hi)//2
        count = 0

        for row in mat:
            # We can implement binary search again as separate function, but bisect_right was employed instead.
            count += bisect_right(row, mid)
        
        if count < desired:
            lo = mid + 1
        else:
            hi = mid
    return lo

import heapq
def findMedianPQ(mat):
    # We need to find the Kth smallest element. We don't need to sort all elements. Instead we can use a min heap. Time complexity: O(r * c + k * log (r * c)), where k = (r * c + 1)// 2 ~ O(r * c * log (r * c))

    all_lst = []
    for row in mat:
        all_lst += row
    
    # O(r * c) time complexity (linear time in terms of number of elements)
    heapq.heapify(all_lst)

    r, c = len(mat), len(mat[0])

    # O(Each pop function takes log(r * c)) time.
    for _ in range((r * c + 1)//2 - 1):
        heapq.heappop(all_lst)
    
    return heapq.heappop(all_lst)




