# Q: https://www.geeksforgeeks.org/n-th-root-number/

def nthRootBS(n, m):
    # Time complexity: O(log N). Space complexity: O(1)
    lo, hi = 1, m
    ans = -1
    while lo <= hi:
        mid = (lo + hi)//2
        if mid ** n == m:
           return mid
        elif mid ** n < m:
            lo = mid + 1
        else:
            hi = mid - 1
    return ans

import math
def nthRootBits(n, m):
    # For a 32 bit integer, time and space complexity: O(32) ~ O(1)
    msb = int(math.log2(m))
    msk = 1 << msb

    ans = 0
    
    # Try to set each bit (starting from most significant bit; msb) if it exceeds m, unset it (using xor)
    while msk:
        ans |= msk
        if ans ** n > m:
            ans ^= msk
        msk >>= 1
    
    if ans ** n != m: return -1
    else: return ans


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(nthRootBS(n, m))
    print(nthRootBits(n, m))