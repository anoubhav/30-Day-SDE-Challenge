
def merge_sorting_editorial(intervals):
    # Ref: https://leetcode.com/problems/merge-intervals/solution/
    # Same logic as my merge_sorting function. But, cleaner.

    intervals.sort(key = lambda x: x[0])
    merged = []

    for curr in intervals:
        if not merged or merged[-1][1] < curr[0]:
            merged.append(curr)
        else:
            merged[-1][1] = max(merged[-1][1], curr[1])
    return merged

def merge_sorting_mine(intervals):
    # Time complexity: O(n log n) for sorting. Space complexity O(1) assuming sorting in place.
    intervals.sort(key = lambda x: x[0]) #in-place sort
    ans = []

    n = len(intervals)
    i = 0

    # O(N) each interval is processed once.
    while i < n:
        curr = intervals[i]
        end = curr[1]
        
        j = i + 1
        while j < n and intervals[j][0] <= end:
            end = max(end, intervals[j][1])
            j += 1
        
        i = j
        ans.append([curr[0], end])
    
    return ans

def usingCC(intervals):
    # Time O(N^2)
    # Build the connection graph
    def dfs(interval, g, count):
        for nbr in g[interval]:
            if nbr not in visited:
                visited.add(nbr)
                mergInt = cc[count]
                cc[count] = [min(mergInt[0], nbr[0]), max(mergInt[1], nbr[1])]
                dfs(nbr, g, count)

    from collections import defaultdict
    g = defaultdict(list)
    n = len(intervals)
    for i in range(n):
        for j in range(i+1, n):
            int1, int2 = intervals[i], intervals[j]
            if int1[0] > int2[0]:
                int1, int2 = int2, int1

            if int1[1] >= int2[0]:
                # they intersect
                g[tuple(int1)].append(tuple(int2))
                g[tuple(int2)].append(tuple(int1))
            else:
                pass
    
    # Calculate the number of connected components in the undirected graph.
    visited = set()
    cc = defaultdict(list)

    count = 0
    for i in intervals:
        interval = tuple(i)
        if interval not in visited:
            visited.add(interval)
            cc[count] = interval

            dfs(interval, g, count)
            count += 1

    return list(cc.values())





# intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals = [[1, 4], [4, 5]]
intervals = [[1, 10], [2, 3], [5, 6], [11, 12]]

# print(usingCC(intervals))
print(merge_sorting_editorial(intervals))