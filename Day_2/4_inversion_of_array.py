# Problem: https://www.hackerrank.com/challenges/ctci-merge-sort/problem
# Ref: https://www.youtube.com/watch?v=owZhw-A0yWE
def naive(arr):
    # O(N^2) time complexity; O(1) space.
    n = len(arr)
    inv = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]: inv += 1
    return inv


def InversionsMergeSort(arr):
    # Time complexity: O(n log n); Space complexity: O(n) - to create the merged array. 
    inv = 0
    def merge(left, right):
        nonlocal inv
        i, j = 0, 0
        merged = []
        n, m = len(left), len(right)
        while i < n and j < m:
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inv += n - i  # key step to count inversions.
                j += 1
        
        while i < n:
            merged.append(left[i])
            i += 1
        while j < m:
            merged.append(right[j])
            j += 1

        return merged

    def mergesort(arr, l, r):
        if r == l:
            return [arr[l]]
        
        mid = (l + r)//2
        left = mergesort(arr, l, mid)
        right = mergesort(arr, mid+1, r)

        return merge(left, right)

    mergesort(arr, 0, len(arr) - 1)
    return inv





arr = [2, 1, 3, 1, 2] 
print(naive(arr))
print(InversionsMergeSort(arr))
