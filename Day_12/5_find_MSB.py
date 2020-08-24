# Ref: https://www.geeksforgeeks.org/find-significant-set-bit-number/

def setBits(num):
    # O(1)

    # Below steps set all bits after MSB
    num |= num >> 1
    num |= num >> 2
    num |= num >> 4
    num |= num >> 8
    num |= num >> 16

    return (num + 1)>>1

def shiftMask(num):
    # O(log num) time
    msk = 1 << 31
    for i in range(31, -1, -1):
        if (num & msk) > 0:
            break
        msk >>= 1
    return 1<<i

def shiftInteger(num):
    # O(log num) time
    i = 0
    while num:
        num >>= 1
        i += 1
    return 1<<(i - 1)

def usingLogs(num):
    from math import log2
    k = int(log2(num)) 
    return 2**k 

num = 1

print(setBits(num))
print(shiftMask(num))
print(shiftInteger(num))
print(usingLogs(num))
