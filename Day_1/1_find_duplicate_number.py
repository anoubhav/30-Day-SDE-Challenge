def sorting(arr):
    # this modifies the array. Time complexity: O(nlogn). Space complexity. O(1)
    arr.sort()
    n = len(arr)
    for i in range(1, n):
        if arr[i] == arr[i-1]:
            return arr[i]

def hashmap(arr):
    # Time complexity: O(n). Space complexity: O(n)
    seen  = set()
    for i in arr:
        if i in seen:
            return i
        else:
            seen.add(i)

def naive(arr):
    # Time complexity: O(n^2). Space complexity: O(1)
    n = len(arr)
    for i in range(n):
        curr = arr[i]
        for j in range(i+1, n):
            if arr[j] == curr:
                return curr

def binarysearch(arr):
    # Time complexity: O(n log n). Space complexity: O(1). This approach does NOT modify the input array. This is a valid solution to given problem constraints. 
    
    def count(arr, num):
        # O(N) time complexity, to get the frequency of elements <= and >= num. No modification is performed.
        le, ge = 0, 0
        for i in arr:
            if i < num: le += 1
            elif i > num: ge += 1
            else:
                le += 1
                ge += 1
        return le, ge
    
    # binary search on the range (1, n). 
    n = len(arr) - 1
    lo, hi = 1, n
    while lo <= hi:
        mid = (lo + hi)//2
        le, ge = count(arr, mid)
        if le + ge > (n + 1) + 1:
            return mid
        elif le > mid:
            hi = mid
        else:
            lo = mid + 1

def floyd_hare_tortoise(arr):
    # https://leetcode.com/problems/find-the-duplicate-number/discuss/72846/My-easy-understood-solution-with-O(n)-time-and-O(1)-space-without-modifying-the-array.-With-clear-explanation./75491

    # Time complexity: O(N). Space complexity: O(1). Does not modify array. Best solution.

    # 1. The first while loop finds a meeting point inside the cycle.
    slow = arr[0]
    fast = arr[arr[0]]
    while slow!=fast:
        slow = arr[slow]
        fast = arr[arr[fast]]
    
    # 2. Finds the starting point of the cycle
    fast = 0
    while fast!=slow:
        fast = arr[fast]
        slow = arr[slow]
    return slow

def extraSpaceArray(arr):
    # Time complexity: O(N). Space complexity: O(N)
    n = len(arr) - 1
    freq = [0]*(n+1)
    for i in arr:
        freq[i] += 1
        if freq[i] > 1:
            return i

arr = [3,1,3,4,2]
print(binarysearch(arr))
print(floyd_hare_tortoise(arr))