# Q: https://leetcode.com/problems/power-of-four/
def usingBits1(num):
    return num!=0 and (num & (num - 1)) == 0 and num.bit_length() & 1

def usingBits2(num):
    return num!=0 and (num & (num - 1)) == 0 and num & 0x55555555

# Every power of 4, is a power of 2. Also, the set bit occurs at odd positions. E.g., bin(4) = 100. or bin(16) = 10000. We check bit_length in first function and we perform and operation with hexadecimal number 0x55555555 in second function. 5: 0101 . It has 1s in odd positions. we create a mask of 0101 0101 0101 0101... 8 times, with 1s at odd positions and perform bitwise AND.

# To understand hexadecimal trick
# https://stackoverflow.com/questions/43923906/what-are-0xaa-and-0x55-doing