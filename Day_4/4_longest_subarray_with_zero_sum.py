def usingMap(n, arr):
    # O(N) time and space.
    ans = 0
    seen = dict()
    
    if arr[0] == 0: 
        ans = 1
    else:
        seen[arr[0]] = 0
    
    pref = arr[0]
    for i in range(1, n):
        pref += arr[i]
        if pref == 0:
            ans = max(ans, i + 1)
        else:
            if pref in seen:
                ans = max(ans, i - seen[pref])
            else:
                seen[pref] = i

    return ans

# the naive solution is O(N^2) time and O(1) space. Simply iterate over all possible sub arrays.