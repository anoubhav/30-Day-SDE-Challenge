def usingBits(num):
    # O(log num) - e.g., 5 * 5 = 5 * (1 0 1) = 5 * (100 + 001) = 5 << 2 + 5 << 0 
    num = abs(num)
    ans = 0
    for i in range(32):
        msk = 1 << i
        if (num & msk) > 0:
            ans += num << i
    return ans
    # We can use this logic to multiply any two number : a * b = a * (binary form of b)

# Ref: https://www.geeksforgeeks.org/calculate-square-of-a-number-without-using-and-pow/
def mathTrickBits(num):
    # O(log num)
    def square(num):
        if num < 0: num = -num
        if num <= 1: 
            return num

        # We reduce the number by half at each step. Similar to binary exponentiation.
        x = num >> 1
        if num & 1: 
            return ((square(x) << 2) + (x<<2) + 1)
        else: 
            return square(x) << 2
    
    return square(num)

def usingOddNums(num):
    # O(num) - N^2 = sum of first N odd numbers
    num = abs(num)
    odd = 1
    s = 0
    while num:
        num -= 1
        s += odd
        odd += 2
    return s

def repeatedAddition(num):
    # O(num)
    num = abs(num)
    s = 0
    for _ in range(num): s += num
    return s

num = -119
print(usingBits(num))
print(mathTrickBits(num))
print(usingOddNums(num))
print(repeatedAddition(num))


