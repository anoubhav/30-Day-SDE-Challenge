def counting_sort(arr):
    # Two-pass algorithm. O(N) time complexity. O(1) space.
    count = [0]*3
    for i in arr:
        count[i] += 1
    
    n = len(arr)
    for i in range(n):
        if count[0]>0:
            arr[i] = 0
            count[0] -= 1
        elif count[1]>0:
            arr[i] = 1
            count[1] -= 1
        else:
            arr[i] = 2
            count[2] -= 1
    return arr


def veryCoolAlgorithm(arr):
    z, o, t = -1, -1, -1
    n = len(arr)
    for i in range(n):
        if arr[i] == 0:
            t += 1
            arr[t] = 2

            o += 1
            arr[o] = 1

            z += 1
            arr[z] = 0
        
        elif arr[i] == 1:
            t += 1
            arr[t] = 2

            o += 1
            arr[o] = 1
        
        else:
            t += 1
            arr[t] = 2
    return arr


# Ref: https://en.wikipedia.org/wiki/Dutch_national_flag_problem
# code: https://leetcode.com/problems/sort-colors/discuss/26481/Python-O(n)-1-pass-in-place-solution-with-explanation
def dutch_NF_algorithm(arr):
    # One-pass algorithm. O(N) time and O(1) space.
    n = len(arr)
    red, white, blue = 0, 0, n-1
    # [0, red) - 0s
    # [red, white) - 1s
    # [white, blue) - unclassified
    # [blue, end] - 2s
    while white <= blue:
        if arr[white] == 1:
            white += 1
        elif arr[white] == 0:
            arr[red], arr[white] = arr[white], arr[red]
            red += 1
            white += 1
        else:
            arr[blue], arr[white] = arr[white], arr[blue]
            blue -= 1
    return arr


arr = [2, 0, 2, 1, 1, 0]
print(counting_sort(arr))
print(dutch_NF_algorithm(arr))
print(veryCoolAlgorithm(arr))