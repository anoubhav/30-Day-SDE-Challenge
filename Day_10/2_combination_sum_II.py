# Q: https://leetcode.com/problems/combination-sum-ii/
def combSumBackTrackDFS(candidates, target):
    # Time complexity: O(2 ^ N), where N is length of candidate. Each element in candidate can be included or not. 
    ans = []
    candidates.sort() # as duplicates are allowed in candidates
    n = len(candidates)

    def recurse(tot, comb, ind, n):
        if tot == 0:
            ans.append(comb.copy())
        else:
            i = ind
            while i < n:
                c = candidates[i]
                if tot - c >= 0:
                                    # each number only used once; Hence, i + 1
                    recurse(tot - c, comb + [c], i + 1, n)

                    # ensure the next no. added to the combination is not same as current, as all possibilities starting from current have been explored. Below loop is only possible by sorting.
                    i += 1
                    while i < n and candidates[i] == c: 
                        i += 1
                else:
                    # sorted candidates
                    break

    recurse(target, [], 0, n)
    return ans

candidates = [10,1,2,7,6,1,5]
target = 8

# candidates = [2,5,2,1,2]
# target = 5

print(combSumBackTrackDFS(candidates, target))

1, 2, 2, 2, 5