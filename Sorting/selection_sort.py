
def selection_sort(array):
    min_num=array[0]
    for i in range(0,len(array)):
        for j in range(i+1,len(array)):
            if array[i]>array[j]:
                min_num=array[j]
                array[j]=array[i]
                array[i] = min_num
    return array

array=[2,8,5,3,9,4,1]
print(selection_sort(array))

