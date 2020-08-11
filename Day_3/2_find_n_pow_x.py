def binaryRecursive(n, x):
    # O(log N) complexity
    if x == 0:
        return 1
    elif x%2:
        return n*binaryRecursive(n, x-1)
    else:
        return binaryRecursive(n, x//2)**2

def binaryIterative(a, b):
    # O(log N) complexity
    result = 1
    while b:
        if b&1: result *= a
        a *= a
        b >>= 1
    return result

def naive(a, b):
    # O(N) time complexity
    ans = 1
    for _ in range(b):
        ans*=a
    return ans