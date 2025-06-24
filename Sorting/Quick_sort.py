


def quicksort(array):

    if len(array)<=1:
        return array
    else:
        pivot=array.pop()

    greater_ele= []
    smaller_ele= []

    for e in array:
        if pivot < e:
            greater_ele.append(e)
        else:
            smaller_ele.append(e)
    return quicksort(smaller_ele)+ [pivot] +quicksort(greater_ele)

array=[0,8,4,7,3,9,1,7,4,7,4,2]
print((quicksort(array)))
