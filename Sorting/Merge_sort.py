

# merge unsorted array
# def merge_unsorted_array(array):
#     if len(array) <= 1:
#         return array
#     mid = len(array)//2
#     left = array[:mid]
#     right = array[mid:]
#
#     #function call recursively until get sorted array
#     left = merge_unsorted_array(left)
#     right = merge_unsorted_array(right)
#
#     return merge_two_sorted_list(left,right)
#
# # merge the Sorted array a and b
# def merge_two_sorted_list(a,b):
#     sorted_list=[]
#     i=j=0
#     while i<len(a) and j<len(b):
#         if a[i]<b[j]:
#             sorted_list.append(a[i])
#             i+=1
#         else:
#             sorted_list.append(b[j])
#             j+=1
#     while i<len(a):
#         sorted_list.append(a[i])
#         i+=1
#     while j<len(b):
#         sorted_list.append(b[j])
#         j+=1
#
#     return sorted_list
#
# a=[3,7,10,15,20,25]
# b=[2,4,8,9,18,24]
# array=[25,22,15,18,13,9,3,8,6]
#
# print(merge_two_sorted_list(a,b))
# print(merge_unsorted_array(array))


######################################################################################################

# merge unsorted array - In this version you don't have to create new list

def merge_unsorted_array(array):
    if len(array) <= 1:
        return array
    mid = len(array)//2
    left = array[:mid]
    right = array[mid:]

    #function call recursively until get sorted array
    merge_unsorted_array(left)
    merge_unsorted_array(right)

    merge_two_sorted_list(left,right,array)


# merge the Sorted array a and b
def merge_two_sorted_list(a,b,array):
    i = j = k = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            array[k] = a[i]
            i += 1
        else:
            array[k] = b[j]
            j += 1

        k += 1
    # One of the halfs will have elements remaining
    while i < len(a):
        array[k] = a[i]
        i += 1
        k += 1

    while j < len(b):
        array[k] = b[j]
        j += 1
        k += 1


test_cases=[
    [1,6,3,9,28,12,30,16,13,18],
    [],
    [2,7,1,9],
    [1,2,3,4],
    [3]
]

for arr in test_cases:
    merge_unsorted_array(arr)
    print(arr)


# array = [25,22,15,18,13,9,3,8,6]
# merge_unsorted_array(array)
# print(array)