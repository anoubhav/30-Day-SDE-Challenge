# Q: https://leetcode.com/problems/combination-sum-iii/solution/
def combSumBackTrack(n, k):
    # Time complexity: O(k * 9!/(9 - k)!).
    # Space complexity : O(k); see solutions tab for more info.
    if n > 45: return [] # (1 + .. + 9)

    candidates = list(range(1, 10))
    length = 9
    ans = []
    def recurse(tot, comb, ind, k, l):
        if tot == 0 and k == 0:
            ans.append(comb.copy())

        elif k <= 0: return

        else:
            i = ind
            while i < l:
                c = candidates[i]
                if tot - c >= 0:
                    recurse(tot - c, comb + [c], i + 1, k - 1, l)
                else: break
                i += 1
    
    recurse(n, [], 0, k, length)
    return ans

def usingLibrary(n, k):
    from itertools import combinations
    return [c for c in combinations(range(1, 10), k) if sum(c) == n]

n, k = 9, 3
print(combSumBackTrack(n, k))