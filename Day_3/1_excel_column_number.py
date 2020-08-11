# Ref: https://leetcode.com/problems/excel-sheet-column-number/discuss/52289/Explanation-in-Python

# 
# Observe that this is basically the same thing as converting between base 26 and base 10.
def titleToNumber(s):

    s = s[::-1]
    ans = 0
    for exp, char in enumerate(s):
        ans += (ord(char) - 65 + 1) * (26 ** exp)
    return ans


# https://leetcode.com/problems/excel-sheet-column-title/discuss/441430/Detailed-Explanation-Here's-why-we-need-n-at-first-of-every-loop-(JavaPythonC%2B%2B)  - Why we do n-1

def convertToTitle(n):
    ans = []
    while(n > 0):
        n -= 1 # convert 1-26 to 0-25
        curr = n % 26
        n = int(n / 26)
        ans.append(chr(curr + ord('A')))
    
    return ''.join(ans[::-1])

