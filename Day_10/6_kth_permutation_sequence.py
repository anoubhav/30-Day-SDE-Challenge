# Q: https://leetcode.com/problems/permutation-sequence/

def getPermutationNaive(n, k):
    # Soln 1: Use the 3_next_permutation.py from Day 2 problem. Starting with array [1..n], run the function k times. Time complexity: O(k * n) , where 1 < k < n!. This gets Accepted but is very slow.
    def nextPermutation(arr):
        # Time complexity: O(N), space complexity: O(1)
        def binarySearch(arr, l, r):
            l = i + 1
            r = n - 1
            while l <= r:
                mid = (l + r)//2
                if arr[i] < arr[mid]:
                    if mid + 1 < n and arr[i] < arr[mid + 1]:
                        l = mid + 1
                    else: 
                        l = mid
                        break
                else:
                    r = mid - 1
            return l

        n = len(arr)
        swap = False
        for i in range(n-2, -1, -1):
            if arr[i] < arr[i + 1]:
                # Find the smallest element after arr[i] which is larger than arr[i]
                ans = binarySearch(arr, i + 1, n - 1)

                # swap this number and the smallest largest number after it.
                arr[i], arr[ans] = arr[ans], arr[i]

                # reverse the array
                j = 0
                while j < (n - (i + 1))//2:
                    arr[i + 1 + j], arr[n-1 - j] = arr[n-1 - j], arr[i + 1 + j]
                    j += 1
                
                swap = True
                break

        if not swap:
            # Reverse the array in O(n)
            i = 0
            while i < n//2:
                arr[i], arr[n-1 - i] = arr[n-1 - i], arr[i]
                i += 1
        return arr

    arr = list(range(1, n + 1))
    for _ in range(k - 1):
        arr = nextPermutation(arr)
    return ''.join([str(i) for i in arr])

# Ref: https://leetcode.com/problems/permutation-sequence/discuss/22507/%22Explain-like-I'm-five%22-Java-Solution-in-O(n)
def getPermutationMath(n, k):
    # Time complexity: O(N^2). Space complexity: O(1). 
    # Note: The deletion step can be optimised by using an ordered dictionary (BST) or some cache. But, here n <= 9. So it is not necessary

    from math import factorial
    prod = factorial(n)
    nums = [str(i) for i in range(1, n+1)]

    digits = ''
    for i in range(n, 1, -1):
        prod = prod//i
        index, k = divmod(k, prod)
        if k == 0: index -= 1
        digits += nums.pop(index)
        # O(N) pop - Remove the element from array at index
        
    return digits + nums[0]

def getPermutationMathRecursive(n, k):
    # Time complexity: O(N^2). Space complexity: O(N) - Recursion stack. 
    import math
    def backtrack(s, rest, k):
        if not rest:
            return s
        for i in range(len(rest)):
            if k > math.factorial(len(rest)-1):
                k -= math.factorial(len(rest)-1)
                continue
            s += rest[i]
                            # creating copy of list is O(N)
            ans = backtrack(s, rest[:i] + rest[i+1:], k)
            if ans: return ans
    
    nums = list(map(str, range(1, n+1)))
    
    return backtrack('', nums, k)    


        
n, k = 9, 1019
print(getPermutationNaive(n, k))
print(getPermutationMath(n, k))
print(getPermutationMathRecursive(n, k))