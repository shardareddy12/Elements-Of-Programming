'''
Input range = [0,1,2,3,4,5,6,7,8,9,10]
Output = [F,F,T,T,F,T,F,T,F,F,F]
T - if prime
F - Not prime
'''
import math

result=[]  # store result of number
def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(math.sqrt(num))+1):  # here we are optimising the calculation using sqrt
        if num%i==0:
            return False
    return True

for i in range(11):
    # Find prime number and if is prime return True else False
    if is_prime(i):
        result.append("T")
        print(i)
    else:
        result.append("F")
print(result)