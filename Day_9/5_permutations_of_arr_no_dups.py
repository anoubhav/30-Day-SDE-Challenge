# Q: https://leetcode.com/problems/permutations/ (NO DUPLICATES)
def permuteBackTrack(arr):
    # Time and space complexity: O(N!)
    n = len(arr)
    ans = []
    def solve(i, n):
        if i == n:
            ans.append(arr.copy())
        else:
            for j in range(i, n):
                arr[i], arr[j] = arr[j], arr[i]
                solve(i + 1, n)
                arr[i], arr[j] = arr[j], arr[i]
    solve(0, n)
    return ans

# Ref: https://leetcode.com/problems/permutations/discuss/18296/Simple-Python-solution-(DFS). See comments to understand the recursive calls. Or https://www.youtube.com/watch?v=KukNnoN-SoY
def permuteDFS(nums):

    def dfs(nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)
            # add nums[i] to path

    res = []
    dfs(nums, [], res)
    return res

def pythonInbuilt(arr):
    from itertools import permutations
    return list(map(list, permutations(arr)))

arr = [1, 2, 3]
print(permuteBackTrack(arr))
print(permuteDFS(arr))
print(pythonInbuilt(arr))

