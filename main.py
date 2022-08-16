def binarySearch(arr,l,r):
    if len(arr) == 0:
        return -1
    elif arr[l] <= arr[r]:
        return l
    mid = l + (r - l) // 2
    if arr[mid] < arr[mid-1]:
        return arr[mid]
    elif arr[mid] < arr[l]:
        return binarySearch(arr, l, mid - 1)
    else:
        return binarySearch(arr, mid + 1, r)


arr1 = [4, 5, 6, 7, 8, 9, 2, 3]
result = binarySearch(arr1, 0, len(arr1) - 1)
if result != -1:
    print("The minimum value in the array is", arr1[result])
else:
    print("The given array is empty")