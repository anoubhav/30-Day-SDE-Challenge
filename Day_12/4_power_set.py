# Q: https://practice.geeksforgeeks.org/problems/power-set/0

# Time complexity for all algorithms to generate powerset is O(2 ** n). However, sorting the powerset(for lexographic order) adds an extra O(2**n + 2 ** n * log (2 ** n)) = O(n * 2 ** n )

def usingBits(n, s):
    powerset = []
    setsize = 2**n
    for i in range(setsize):
        subset = ''
        for j in range(n):
            if (1 << j) & i:
                subset += s[j]
        powerset.append(subset)

    return sorted(powerset) # to obtain lexographic order

def usingRecursion(n, s):
    powerset = []
    def recurse(s, perm):
        if s == '':
            powerset.append(perm)
            return
        # include
        recurse(s[1:], perm)
        # don't include
        recurse(s[1:], perm + s[0])

    recurse(s, '')
    return sorted(powerset)

def usingPython(n, s):
    from itertools import combinations
    setsize = 2 ** n
    powerset = []
    for i in range(setsize):
        for comb in combinations(s, i):
            powerset.append(''.join(comb))
    return sorted(powerset)

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    powset = usingBits(n, s[:n])
    powset = usingRecursion(n, s[:n])
    powset = usingPython(n, s[:n])
    print(*powset[1:]) # print all, except null set
    
