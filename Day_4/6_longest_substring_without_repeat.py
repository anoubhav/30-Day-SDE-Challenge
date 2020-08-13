def usingSet(s):
    # Time complexity: O(N); space : O(min(m, N)). Here, N is the length of the string and m is the size of the alphabet. 

    # In our case m = 26, thus, the space complexity = O(26) ~ O(1)

    # In the worst case each character will be visited twice.
    seen = set()
    n = len(s)
    ans = i = j = 0
    while i < n and j < n:
        if s[j] in seen:
            seen.remove(s[i])
            i += 1
        else:
            seen.add(s[j])
            j += 1
            ans = max(ans, j - i)
    return ans

def usingMapOptimised(s):
    # Time complexity: O(N); space : O(min(m, N)). Here, N is the length of the string and m is the size of the alphabet. 
    # Worst case N steps. (not 2N steps like other solutions)
    seen = dict()
    n = len(s)
    start = i = ans = 0
    while i < n:
        char = s[i]
        if char in seen:
            move = seen[char] + 1
            if move > start:
                start = move
        seen[char] = i
        ans = max(ans, i - start + 1)
        i += 1
    return ans


def usingMap(s):
    # Time complexity: O(N); space : O(min(m, N)). Here, N is the length of the string and m is the size of the alphabet. 

    # In our case m = 26, thus, the space complexity = O(26) ~ O(1)

    # In the worst case each character will be visited twice.
    n = len(s)
    if n < 2: return n

    seen = dict()
    slow = 0
    seen[s[0]] = 0

    ans = 1
    for fst in range(1, n):
        char = s[fst]
        if char in seen:
            ans = max(ans, fst - slow)
            t = seen[char]
            while slow <= t:
                del seen[s[slow]]
                slow += 1
        seen[char] = fst
    return max(ans, fst - slow + 1)        

