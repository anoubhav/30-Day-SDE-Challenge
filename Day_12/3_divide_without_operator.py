# Q: https://leetcode.com/problems/divide-two-integers/

# The key observation is that the quotient of a division is just the number of times that we can subtract the divisor from the dividend without making it negative.

# a/b--> a is dividend and b is divisor

def repeatedSubtraction(a, b):
    # Time: O(a) - TLE
    quo = 0
    sign = (a > 0) == (b > 0)

    a, b = abs(a), abs(b)
    while b < a:
        a -= b
        quo += 1

    # a is the remainder
    return quo if sign else -quo

# Ref: https://leetcode.com/problems/divide-two-integers/discuss/13407/C%2B%2B-bit-manipulations
def usingBits(a, b):
    # Int--> [-2**31, 2 ** 31 - 1]
    if (a == -2147483648 and b == -1): return 2147483647

    # Time: O(log a)
    quo = 0
    temp = 0
    sign = (a > 0) == (b > 0)
    a, b = abs(a), abs(b)
    
    for i in range(31, -1, -1):
        if (temp + (b << i)) <= a:
            temp += b << i
            quo |= 1<<i

    return quo if sign else -quo
    

a, b = -89, -3
print(repeatedSubtraction(a, b))
print(usingBits(a, b))