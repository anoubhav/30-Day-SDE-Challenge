# Ref: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/39038/Kadane's-Algorithm-Since-no-one-has-mentioned-about-this-so-far-%3A)-(In-case-if-interviewer-twists-the-input)
def kadaneCreateDifferenceArray(arr):
    # Time complexity: O(N); space complexity : O(N)
    # Find the maximum subarray sum on the difference array.
    n = len(arr)
    diff = arr.copy()
    for i in range(1, n):
        diff[i] = arr[i] - arr[i-1]
    
    ans = msf = 0
    for i in range(1, n):
        msf = max(msf + diff[i], diff[i])
        ans = max(ans, msf)
    return ans

def kadane(arr):
    # Time complexity: O(N), space complexity: O(1)
    ans = msf = 0
    for i in range(1, len(arr)):
        msf = max(msf + prices[i] - prices[i-1], 0)
        ans = max(ans, msf)
    return ans

def minimaMaxima(arr):
    # Time complexity: O(N), space complexity: O(1)
    minprice = 10**6
    maxprofit = 0
    n = len(arr)
    for i in range(n):
        if arr[i] < minprice:
            minprice = arr[i]
        
        elif arr[i] - minprice > maxprofit:
            maxprofit = arr[i] - minprice
    return maxprofit

arr = [7,1,5,3,6,4]
print(kadane(arr))
print(minimaMaxima(arr))