def naive(nums, target):
    # O(N^4) time complexity; O(1) space complexity.
    n = len(nums)
    ans = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        ans.add(tuple(sorted((nums[i], nums[j], nums[k], nums[l]))))
    return list(ans)

def usingMap(nums, target):
    # O(N^3) time complexity; O(N) space
    n = len(nums)
    
    hashmap = dict()
    for i, num in enumerate(nums):
        hashmap[num] = i
    
    ans = set()
    seen = set()
    a = 0
    while a < n - 3:
        curr = nums[a]
        if curr in seen:
            a += 1
            continue
        seen.add(curr)
        
        for b in range(a + 1, n - 2):
            for c in range(b + 1, n - 1):
                s = nums[a] + nums[b] + nums[c]
                d = target - s
                if d in hashmap:
                    if hashmap[d] > c:
                        ans.add(tuple(sorted([nums[a], nums[b], nums[c], d])))
        a += 1

    return list(ans)

def usingTwoPointer(nums, target):
    n = len(nums)
    nums.sort()
    ans = set()
    for a in range(n):
        if a == 0 or nums[a]!=nums[a-1]:
            for b in range(a + 1, n):
                if b == a+1 or nums[b] != nums[b-1]:
                    s = target - (nums[a] + nums[b])
                    lo, hi = b + 1, n - 1
                    while lo < hi:
                        if nums[lo] + nums[hi] < s or (lo > b+1 and nums[lo] == nums[lo - 1]):
                            lo += 1
                        elif nums[lo] + nums[hi] > s or (hi < n - 1 and nums[hi] == nums[hi + 1]):
                            hi -= 1
                        else:
                            ans.add((nums[a], nums[b], nums[lo], nums[hi]))
                            lo += 1
                            hi -= 1
    return ans

nums = [1, 0, -1, 0, -2, 2]
target = 0

print(naive(nums, target))
print(usingMap(nums, target))
print(usingTwoPointer(nums, target))
