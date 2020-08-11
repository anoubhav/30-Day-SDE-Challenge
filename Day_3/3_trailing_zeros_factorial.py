# https://www.purplemath.com/modules/factzero.htm
n = int(input())
ans = 0
for i in range(1, 18):
    t = n//pow(5, i)
    if t == 0: break
    ans += t
print(ans)