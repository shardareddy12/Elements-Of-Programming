# Dutch Flag
# Rearrange the element

array = [0, 1, 2, 0, 2, 1, 1,0]
pivot = 2


def dutchflag(array, pivot):
    pivot_val = array[pivot]
    smaller, equal , larger = 0,0,len(array)

    while equal<larger:
        if pivot_val > array[equal]:
            array[smaller],array[equal] = array[equal],array[smaller]
            equal+=1
            smaller+=1
        elif array[equal]==pivot_val:
            equal+=1
        else:
            array[equal], array[larger] = array[larger], array[equal]
            larger -= 1

    return array


#__________________solution 1_____________________
#Complexity space =O(n) and time complexity = O(n)

# left_arr = []
# right_arr = []
# def dutchflag(array,pivot):
#     for i in range(0,len(array)):
#         if array[pivot] >array[i]:
#             left_arr.append(array[i])
#         else:
#             right_arr.append(array[i])

#     return left_arr + (right_arr)


# res = dutchflag(array,pivot)
# print(res)


#-------------------Solution 2-------------------------------
#time complexity = O(n) Space Complexity = O(1)

# def dutchflag(array, pivot):
#     pivot_val = array[pivot]
#     smaller = 0
#     for i in range(0, len(array)):
#         if pivot_val > array[i]:
#             array[i], array[smaller] = array[smaller], array[i]
#             smaller += 1
#         # print(array)
#         # print("--")
#
#     larger = len(array) - 1
#     for j in reversed(range(len(array))):
#         if pivot_val < array[j]:
#             array[j], array[larger] = array[larger], array[j]
#             larger -= 1
#         print(array)
#
#     return array


res = dutchflag(array, pivot)
print(res)

