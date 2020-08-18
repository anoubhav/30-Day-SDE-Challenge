# Ref: https://www.youtube.com/watch?v=vtJvbRlHqTA
# https://leetcode.com/problems/maximum-product-subarray/discuss/48276/Python-solution-with-detailed-explanation
def maxProdSubarray_Kadane(arr):
    # O(N) time. O(1) space
    prevmax, prevmin, currmax, currmin = arr[0], arr[0], arr[0], arr[0]
    ans = currmax
    for num in arr:
        currmax = max(prevmax * num, prevmin * num, num)
        currmin = min(prevmax * num, prevmin * num, num)
        ans = max(ans, currmax)
        prevmax = currmax
        prevmin = currmin
    return ans

    # Proof for maxProdSubarray_Kadane: Recall what we did in Maximum Subarray Sum (Kadane algorithm), only known maximum ends at i-1 is not enough for this max multiply.

    # Due to negative number and property of multiply, we need max and min ends at i-1 in case negative number at i causes them swap. Therefore, we maintain two local optimal variables, update them in each iteration and the global maximum as well.

def prefixSuffix_Kadane(nums):
    # This algorithms is based on one conclusion: the max product must either start with 0 or end with n-1. or 1 handles the case when prefix prod is 0. It sets future prefix product back to 1. e.g., [2, 3, 0, 7, 9]

    prefix, suffix, max_so_far = 0, 0, float('-inf')
    for i in range(len(nums)):
        prefix = (prefix or 1) * nums[i]
        suffix = (suffix or 1) * nums[~i]
        max_so_far = max(max_so_far, prefix, suffix)
    return max_so_far


    # Proof for Prefix Suffix: https://leetcode.com/problems/maximum-product-subarray/discuss/183483/JavaC++Python-it-can-be-more-simple/502936