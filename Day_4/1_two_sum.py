def usingMap(nums, target):
    # O(N) time and space
    hashmap = dict()
    for i, num in enumerate(nums):
        if target - num in hashmap:
            return [hashmap[target - num], i]
        hashmap[num] = i
    return -1

def twoPointer(nums, target):
    # O(n log n) time complexity, O(n) space
    og = nums.copy()
    nums.sort()
    n = len(nums)
    i, j = 0, n - 1
    answer = None
    while i < j:
        if nums[i] + nums[j] > target:
            j -= 1
        elif nums[i] + nums[j] < target:
            i += 1
        else:
            answer = (nums[i], nums[j])
            break
    
    indices = []
    for i, num in enumerate(og):
        if num in answer:
            indices.append(i)

    return indices

def naive(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return -1


nums = [2, 7, 11, 15]
target = 9

print(naive(nums, target))
print(usingMap(nums, target))
print(twoPointer(nums, target))