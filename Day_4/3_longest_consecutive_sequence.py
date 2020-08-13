def usingSort(nums):
    # Time complexity: O(n log n). Space complexity: O(1)
    n = len(nums)
    if n < 2:
        return n

    nums.sort()
    ans = 0
    
    count = 1
    for i in range(1, n):
        if nums[i] == nums[i-1] + 1:
                count += 1
        else:
            if nums[i] > nums[i-1] + 1:
                count = 1
        ans = max(ans, count)
    return ans

def usingMap(nums):
    if not nums: return 0
    # Time complexity: O(n). Space complexity: O(n)
    present = set(nums)
    
    ans = 1
    n = len(nums)
    for i in range(n):
        curr = nums[i]
        # we only attempt to build sequences from numbers that are not already part of a longer sequence. This is accomplished by first ensuring that the number that would immediately precede the current number in a sequence is not present, as that number would necessarily be part of a longer sequence.
        if curr - 1 not in present:
            count = 1
            t = curr
            while t + 1 in present: # O(1) look up
                count += 1
                t += 1
            ans = max(ans, count)
    return ans

arr = [100, 4, 200, 1, 3, 2]
print(usingSort(arr))
print(usingMap(arr))