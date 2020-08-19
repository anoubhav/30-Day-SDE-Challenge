# Q: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
def findMinArrowShots(points):
    if not points: return 0

    # Sort by finishing times. Optimal to pick the right most end point of balloon to shoot the arrow
    points.sort(key = lambda x: x[1])
    count = 1
    prev = points[0][1]

    for pt in points[1:]:
        if pt[0] > prev:
            count += 1
            prev = pt[1]
        else:
            pass
    return count


# Similar problem:
# https://leetcode.com/problems/non-overlapping-intervals/submissions/
def eraseOverlapIntervals(intervals):
    if not intervals: return 0
    intervals.sort(key = lambda x: x[1])
    count = 0
    prev = intervals[0][1]
    
    for pt in intervals[1:]:
        if pt[0] >= prev:
            prev = pt[1]
        else:
            count += 1
    return count