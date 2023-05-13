def mergesort(array):
    if len(array) > 1:
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        mergesort(L)
        mergesort(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k = k + 1

        while i < len(L):
            array[k] = L[i]
            k = k +1
            i += 1
        while j < len(M):
            array[k] = M[j]
            k = k + 1
            j += 1




#array = input("Enter the array").split()
array = [5, -1, 4, 1, 2]
mergesort(array)
print(array)







