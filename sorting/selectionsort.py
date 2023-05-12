def selectionsort(array):

    for i in range(len(array)):
        min = i
        for j in range(i, len(array)):
            if array[j] < array[min]:
                min = j
        temp = array[i]
        array[i] = array[min]
        array[min] = temp

    print(array)

arra = [-2, 3, 1, 0]
selectionsort(arra)


