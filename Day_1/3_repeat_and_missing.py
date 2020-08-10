def frequencyArr(arr):
    # O(N) time complexity. O(N) space complexity. Two-pass with extra space.
    n = len(arr)
    freq = [0]*(n+1)
    for i in arr:
        freq[i] += 1
    
    doub, miss = None, None
    for num, i in enumerate(freq):
        if i == 2:
            doub = num
        elif i == 0:
            miss = num 

    return doub, miss

def usingSet(arr):
    # O(N) time complexity. O(N) space complexity.
    n = len(arr)
    doub = sum(arr) - sum(set(arr))
    diff = sum(arr) - n*(n+1)//2   # doub - miss
    return doub, doub - diff

def pureMath(arr):
    # O(N) time complexity. O(1) space complexity.
    n = len(arr)
    s1 = sum(arr)
    sn = (n*(n+1))//2

    s2 = 0
    for i in arr:
        s2 += i**2
    
    s2n = (n*(n+1)*(2*n + 1))//6

    # doub - miss
    diff = s1 - sn

    # doub + miss: (d^2 - m^2)/(d - m) = (d + m)
    summ = (s2 - s2n)//diff

    return (diff + summ)//2, (summ - diff)//2

def traverseMark(arr):
    # O(N) time complexity. O(1) space. But, this modifies the array.
    n = len(arr)
    doub, miss = None, None
    for i in range(n):
        if arr[abs(arr[i]) - 1] > 0:
            arr[abs(arr[i]) - 1] *= -1
        else:
            doub = abs(arr[i])
    
    for i in range(n):
        if arr[i] > 0: miss = i + 1
    
    return doub, miss

# Ref: https://www.geeksforgeeks.org/find-a-repeating-and-a-missing-number/
def usingXOR(arr):
    def rightMostSetBit(num):
        i = 1
        while num & 1 != 1:
            num >>= 1
            i += 1
        return i
    
    n = len(arr)
    xor = 0
    for i in arr:
        xor ^= i
    
    for i in range(1, n+1):
        xor ^= i
    
    # xor = doub ^ miss. A bit is set either in doub OR in miss. 

    rghtsetbit = rightMostSetBit(xor)
    msk = 1 << (rghtsetbit - 1)

    ## Another method to obtain mask directly; without finding right most set bit one by one in loop. Ref: https://www.youtube.com/watch?v=4qH4unVtJkE&list=PLowKtXNTBypGqImE405J2565dvjafglHU&index=14;  https://catonmat.net/low-level-bit-hacks; https://stackoverflow.com/a/37512821
    # msk = xor & ~(xor - 1)   ## uses 1's complement
    # msk = xor & -xor     ## uses 2's complement 
    
    x, y = 0, 0
    for i in arr:
        if i & msk:
            x ^= i
        else:
            y ^= i

    for i in range(1, n+1):
        if i & msk:
            x ^= i
        else:
            y ^= i

    # To find the doub and miss in single pass
    for i in arr:
        if i == x:
            return x, y
        if i == y:
            return y, x

arr = [3, 1, 2, 5, 4, 6, 8, 9, 9]

print(frequencyArr(arr))
print(usingSet(arr))
print(pureMath(arr))
print(traverseMark(arr.copy()))
print(usingXOR(arr))