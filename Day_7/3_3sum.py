def usingHashmap(nums):
    # Time complexity: O(N^2). Space complexity: O(N)
    nums.sort()
    
    ispresent = dict()
    for i, num in enumerate(nums):
        ispresent[num] = i
    
    n = len(nums)
    ans = []
    preva = -10**9
    for i in range(n):
        a = nums[i]
        if a == preva:
            continue
        preva = a
        
        prevb = -10**9
        for b in range(i + 1, n):
            if nums[b] == prevb: continue
            target = -(a + nums[b])
            if target in ispresent and ispresent[target] > b:
                ans.append([a, nums[b], target])
                
            prevb = nums[b]
    return ans

def usingTwoPointers(nums):
    # Time complexity: O(N^2). Space complexity: O(1)
    nums.sort()
    n = len(nums)

    ans = []
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]: continue
        target = -nums[i]

        l, r = i + 1, n - 1
        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                ans.append([-target, nums[l], nums[r]])
                while l < r and nums[l] == nums[l+1]: l += 1
                while l < r and nums[r] == nums[r-1]: r -= 1
                l, r = l + 1, r - 1
                
            if s < target:
                l += 1
                
            if s > target:
                r -= 1
                
    return ans
