array = [1,2,9,9]
'''output = [1,3,0,0] - add 1 in last digit
-Add one in last digit of array if number is less than 9 else 
replace last digit to zero if digit is equal to nine (9+1 = 10) carry is 1.
'''

def add_int_one(array):
    for i in range(len(array)-1,-1,-1):
        if array[i]!=9:
            array[i]+=1
            break
        else:
            array[i] = 0
    return array
res = add_int_one(array)
print(res)