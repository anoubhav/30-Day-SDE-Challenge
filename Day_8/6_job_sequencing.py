# Q: https://practice.geeksforgeeks.org/problems/job-sequencing-problem/0

def jobSequencing():
    # Time complexity: O(N^2). Space complexity: O(N).

    t = int(input())
    for _ in range(t):
        n = int(input())
        values = list(map(int, input().split()))
        jobs = []
        maxded = 0
        for start in range(0, 3*n, 3):
            jobs.append((values[start + 1], values[start + 2]))
            maxded = max(maxded, values[start + 1])
        
        # O(N log N)
        jobs.sort(key = lambda x: x[1], reverse = True)
        
        # visited slot
        slots = [-1]*(1 + maxded)
        
        count, tot = 0, 0

        # O(N^ 2)
        for job in jobs:
            ded, prof = job
            
            for i in range(ded, 0, -1):
                if slots[i]==-1:
                    slots[i] = 1
                    count += 1
                    tot += prof
                    break
        print(count, tot)