# The algorithm which I figured out:
#     1. Find the largest index k such that nums[k] < nums[k + 1]. If no such index exists, just reverse nums and done.
#     2. Find the largest index l > k such that nums[k] < nums[l].
#     3. Swap nums[k] and nums[l].
#     4. Reverse the sub-array nums[k + 1:].

def nextPermutation(arr):
    # Time complexity: O(N), space complexity: O(1)
    def binarySearch(arr, l, r):
        l = i + 1
        r = n - 1
        while l <= r:
            mid = (l + r)//2
            if arr[i] < arr[mid]:
                if mid + 1 < n and arr[i] < arr[mid + 1]:
                    l = mid + 1
                else: 
                    l = mid
                    break
            else:
                r = mid - 1
        return l

    n = len(arr)
    swap = False
    for i in range(n-2, -1, -1):
        if arr[i] < arr[i + 1]:
            # Find the smallest element after arr[i] which is larger than arr[i]
            ans = binarySearch(arr, i + 1, n - 1)

            # swap this number and the smallest largest number after it.
            arr[i], arr[ans] = arr[ans], arr[i]

            # reverse the array
            j = 0
            while j < (n - (i + 1))//2:
                arr[i + 1 + j], arr[n-1 - j] = arr[n-1 - j], arr[i + 1 + j]
                j += 1
            
            swap = True
            break

    if not swap:
        # Reverse the array in O(n)
        i = 0
        while i < n//2:
            arr[i], arr[n-1 - i] = arr[n-1 - i], arr[i]
            i += 1
    return arr

arr = [1,5,1]
print(nextPermutation(arr))
