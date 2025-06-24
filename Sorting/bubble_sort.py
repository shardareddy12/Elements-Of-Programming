
array=[8,5,7,3,2]

def bubble_sort(array):
    # for j in range(len(array)):
    #     for i in range(0,len(array)-1-j):
    #
    #         if array[i]>array[i+1]:
    #             array[i+1],array[i]=array[i],array[i+1]

    sorted=False
    while not sorted:
        sorted=True
        for i in range(0, len(array) - 1):
            if array[i]>array[i+1]:
                sorted=False
                array[i+1],array[i]=array[i],array[i+1]

    return array

print(bubble_sort(array))