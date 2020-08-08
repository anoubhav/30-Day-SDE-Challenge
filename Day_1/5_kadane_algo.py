def naive(arr):
    # Time complexity: O(N^2). Space complexity: O(1)
    # Find all subarrays
    ans = arr[0]
    n = len(arr)
    for i in range(n):
        t = 0
        for j in range(i, n):
            t += arr[j]
            ans = max(ans, t)
    return ans

def kadaneDP(arr):
    # Ref: https://leetcode.com/problems/maximum-subarray/discuss/20193/DP-solution-and-some-thoughts

    # subproblem: dp[i] = maximum subarray sum ending at arr[i]. Then dp[i+1] = max(dp[i] + arr[i], arr[i])

    # Time complexity: O(N), Space complexity: O(1)
    ans = msf = arr[0]
    for i in arr[1:]:
        msf = max(msf + i, i)
        ans = max(msf, ans)
    return ans

def divideConquerNlogN(arr):
    # Time complexity: O(n log n). Space complexity: O(1)
    # Ref: https://www.geeksforgeeks.org/maximum-subarray-sum-using-divide-and-conquer-algorithm/
    
    def crossover(arr, l, m, r):
        # O(N)
        msf, ls = 0, -10**9
        for i in range(m, l-1, -1):
            msf += arr[i]
            ls = max(ls, msf)
        
        msf, rs = 0, -10**9
        for i in range(m+1, r+1):
            msf += arr[i]
            rs = max(rs, msf)
        return max(ls, rs, ls + rs)

    def maxSubarraySum(arr, l, r):
        if l == r:
            return arr[l]
        m = (l + r)//2
        return max(maxSubarraySum(arr, l, m), maxSubarraySum(arr, m+1, r), crossover(arr, l, m, r))

    n = len(arr)
    return maxSubarraySum(arr, 0, n-1)

# Ref: https://leetcode.com/problems/maximum-subarray/discuss/199163/Python-O(N)-Divide-and-Conquer-solution-with-explanations
def divideConquerLinear(arr):
    # a: max subarray sum including the first element
    # b: max subarray sum including the last element
    # m: max subarray sum
    # s: total sum of array
    def maxSubarraySum(arr, l, r):
        if l == r:
            t = arr[l]
            return t, t, t, t
        
        mid = (l + r)//2

        al, bl, ml, sl = maxSubarraySum(arr, l, mid) # max subarray in left half
        ar, br, mr, sr = maxSubarraySum(arr, mid+1, r) # max subarray in right half

        # max subarray sum (left, right, AND crossover)
        a = max(al, sl + ar)
        b = max(br, sr + bl)
        m = max(ml, mr, bl + ar)
        s = sl + sr

        return a, b, m, s

    _, _, ans, _ = maxSubarraySum(arr, 0, len(arr) - 1)
    return ans


arr = [-2,1,-3,4,-1,2,1,-5,4]
print(naive(arr))
print(kadaneDP(arr))
print(divideConquerNlogN(arr))
print(divideConquerLinear(arr))



### Analysis of Divide and Conquer solutions:
# 1. O(N log N) from GFG:
# Return the maximum of following three
#   a) Maximum subarray sum in left half (Make a recursive call) - O(1)
#   b) Maximum subarray sum in right half (Make a recursive call) - O(1)
#   c) Maximum subarray sum such that the subarray crosses the midpoint. - O(N)

# 2. O(N) from LC:
# The main differenc is that step c) (in above GFG) the subarray that crosses midpoint, is computed in **O(1)** as well. By defining four terms: max subsum with first elem, max subsum with last elem, max subsum and sum. BEAUTIFUL.