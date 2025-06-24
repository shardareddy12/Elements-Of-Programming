'''
remove duplicate from array

/Elements Of Programming

Variant 1 = /occurence_key_rem.py
Variant 2 = /occurence_key_rem.py


- start checking number from index 1
- take two variables i, j
- In i (it's index of unique var) store the unique variables
- j for iterating the array
- check one number with previous number (j with j-1)
- if numbers are different , replace with unique index number and increase the unique index by one
- if numbers are same then pass the iteration, and unique index won't move.

input : [1,2,2,3,4,5,5]
output : [1,2,3,4,5]

1st iteration:

i=2
input : [1,2,2,3,4,5,5]
output : [1,2,2,3,4,5,5]

2nd iteration:

i=2
input : [1,2,2,3,4,5,5]
output : [1,2,2,3,4,5,5]

3rd iteration:

i=3
input : [1,2,2,3,4,5,5]
output : [1,2,3,3,4,5,5]

4th iteration:

i=4
input : [1,2,2,3,4,5,5]
output : [1,2,3,4,4,5,5]

5th iteration:

i=5
input : [1,2,2,3,4,5,5]
output : [1,2,3,4,5,5,5]

'''


num= [1,2,2,3,4,5,5,6,6,7]
def removedup(num):
    i=1
    for j in range(1,len(num)):
        if num[j]!=num[j-1]:
            num[i]= num[j]
            i+=1
        # print(num)
        # print(i)
    return i

print(removedup(num))

# def sol2(nums):
#     i=0
#     j=0
#     u=1
#     while (j < len(num)):
#         if nums[i] == nums[j]:
#             j+=1
#             continue
#         i+=1
#         u+=1
#         nums[i], nums[j] = nums[j], nums[i]
#         j+=1
#     return nums[0:u]
#
# print(sol2(num))


