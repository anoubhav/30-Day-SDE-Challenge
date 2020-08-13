def countXOR(arr, target):
    n = len(arr)

    pref = [0]*n
    seen = dict()
    pref[0] = arr[0]
    seen[pref[0]] = 1

    for i in range(1, n):
        pref[i] = pref[i-1] ^ arr[i]
        seen[pref[i]] = seen.get(pref[i], 0) + 1

    count = 0
    for i in range(n):
        prod = pref[i] ^ target

        if prod in seen:
            count += seen[prod]

        if pref[i] == target:
            count += 1

    return count

arr = [5, 6, 7, 8, 9]
target = 5

print(countXOR(arr, target))