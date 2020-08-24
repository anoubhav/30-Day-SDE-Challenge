# Q: https://leetcode.com/problems/combination-sum/

def combSumBackTrackDFS(candidates, target):
    # Time complexity: O(l ^ q). l is the length of candidates. q is (target / smallest candidate). We have at most l choices each time we pick a number ot achieve the target. We make this choice (target/ smallest candidate) number of times in the worst case.
    ans = []
    n = len(candidates)

    def recurse(tot, comb, ind, n):
        if tot == 0:
            ans.append(comb.copy())
        else:
            i = ind
            while i < n:
                c = candidates[i]
                if tot - c >= 0:
                    recurse(tot - c, comb + [c], i, n)
                i += 1
    recurse(target, [], 0, n)
    return ans

candidates = [10,1,2,7,6,1,5]
target = 8

# candidates = [2,5,2,1,2]
# target = 5

print(combSumBackTrackDFS(candidates, target))