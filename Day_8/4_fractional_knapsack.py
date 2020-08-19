# Q: https://practice.geeksforgeeks.org/problems/fractional-knapsack/0
def fractional_knapsack():
    # Time complexity: O(n log n). Space complexity: O(N)
    t = int(input())
    for _ in range(t):
        n, W = map(int, input().split())
        inp = list(map(int, input().split()))
        weights = inp[1::2]
        values  = inp[0::2]
        
        ratios = [0]*n
        for i, tup in enumerate(zip(weights, values)):
            w, v = tup
            ratios[i] = (i, v/w)
        
        ratios.sort(key = lambda x: x[1], reverse = True)
        
        ans = 0

        for item in ratios:
            ind, ratio = item
            w, v = weights[ind], values[ind]
            if w >= W:
                ans += W*ratio
                W = 0
                break
            else:
                ans += v
                W -= w
        print(round(ans, 2))
                
        