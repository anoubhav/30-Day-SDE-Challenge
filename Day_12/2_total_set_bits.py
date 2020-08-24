# Q: https://leetcode.com/problems/number-of-1-bits/

def usingDivision(num):
    # For 32-bit integer: O(1). In general: O(log num)
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count

def shiftingMask(num):
    # For 32-bit integer: O(1). In general: O(log num)
    count = 0
    msk = 1
    while msk <= num:
        count += (num & msk)!=0
        msk <<= 1
    return count

def flipLSB(num):
    # Repeatedly flip the LSB from 1 to 0, until it is 0.
    count = 0
    while num:
        num &= num-1
        count += 1
    return count
        
def usingPython(num):
    return bin(num).count('1')

num = 33
print(usingDivision(num))
print(shiftingMask(num))
print(flipLSB(num))
print(usingPython(num))