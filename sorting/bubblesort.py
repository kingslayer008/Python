

def bubblesort(array):

    for i in range(len(array)):
        swapped = False

        for j in range(0, len(array) -i -1):
            if array[j] > array[j+1]:
                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp
                swapped = True

        if swapped is False:
            break

    print(array)

array = input().split()
bubblesort(array)