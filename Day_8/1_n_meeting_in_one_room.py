# Q: https://www.interviewbit.com/problems/meeting-rooms/. Same as Problem 5.

def solve(self, A):
    n = len(A)
    new = [0]*2*n
    for i in range(n):
        s, e = A[i]
        new[2*i], new[2*i + 1] = (s, 's'), (e, 'e')
    
    new.sort(key = lambda x: (x[0], x[1]))
    # print(new)
    count, ans = 0, 0
    for i in new:
        count += 1 if i[1] == 's' else -1
        ans = max(ans, count)
    return ans