# Q: https://leetcode.com/problems/power-of-two/

# Check if number is a power of 2 in O(1) time.
def usingAND(num):
    # O(1) - Decrement and Compare
    # num = 0 is special case
    #  x – 1 has a 0 in position n when n is a power of 2.
    #  x - 1 has a 1 in position n when n is NOT a power of 2.
    return num!=0 and (num & num-1) == 0

    # This is classical bit manipulation problem for n & (n-1) trick, which removes the last non-zero bit from our number

def usingDivision(num):
    # O(log num) ~ O(1) for 32 bit number
    while num&1 == 0 and num:
        num >>= 1
    return num == 1

def usingTwosComplement(num):
    # O(1) - Complement and Compare
    return num!=0 and (num & -num) == num

    # -num is the 2's complement of num. It is equal to ~num + 1.
    # i.e., negation of the bits of num + 1.

def usingLog(num):
    # O(1). But logs can have floating point errors
    from math import log2
    return num!=0 and 2 ** int(log2(num)) == num


num = 256
print(usingAND(num))
print(usingDivision(num))
print(usingTwosComplement(num))
print(usingLog(num))

# Twos complement and bitwise AND functions are really fast. See article below.

# Ref: https://www.exploringbinary.com/ten-ways-to-check-if-an-integer-is-a-power-of-two-in-c/