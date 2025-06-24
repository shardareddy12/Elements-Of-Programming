

def insertion_sort(array):
    for i in range(1,len(array)):
        print(array[i])
        print(array[i-1])
        while array[i-1]>array[i]:
            array[i-1],array[i]=array[i],array[i-1]
            i=i-1

    return array

array=[1,3,5,2,7]
print(insertion_sort(array))

