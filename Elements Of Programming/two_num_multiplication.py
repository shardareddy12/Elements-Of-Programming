
'''
two Number multiplication 123 * 987 = 121401
123*7 = 861
123*8*10 = 9840
123*9*100 = 110700

861+9840+110700 = 121401

input :
 num1=[1,2,3] num2=[9,8,7]

output:
 121401

'''

# ----------------------------------Solution 1------------------------------------
# a=123
# b=987
#
# def multiply(a,b):
#     res=0
#     for _ in range(b):
#         res+=a
#     if b>=0:
#         return res
#     else:
#         return -res
#
# print(multiply(a,b))

# ----------------------------------Solution 2------------------------------------

a = [1, 2, 3]
b = [-7, 8, 6]

def list_to_int(lst):
    return int(''.join(map(str, lst)))

def multiply_num(a,b):
    length_b = len(b)
    a = list_to_int(a)
    b = list_to_int(b)
    res = 0
    place = 1

    for _ in range(length_b):
        digit = b % 10         # getting last digit of number
        res += a*digit*place   # adding multiplied number to a result
        b = b//10              # drop last digit after multiplying to a number
        place = place*10       # place increasing by 10**1 each time when digit drop one by one from last
    return res if b >= 0 else -res

print(multiply_num(a,b))




