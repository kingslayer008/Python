def binarysearch(array, x, low, high):
    if low <= high:

        mid = low + (high - low)//2
        if array[mid] == x:
            return array[mid]

        elif x < array[mid]:
            return binarysearch(array, x, low, mid-1)

        else:
            return binarysearch(array, x, mid+1, high)
    else:
        return -1


def binarysearchit(array, x, low, high):
    while low <= high:
        mid = low + (high-low)//2
        if array[mid] == x:
            return array[mid]
        elif x < array[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


array = [1, 2, 3, 4, 5, 6]
x = 1
print(binarysearchit(array, x, 0, len(array)-1))




