'''
Find Prime number from range 1-100
- number should only divisible by 1 and itself
Logic - 1. check number is less than 2 if it's 1 and 0 then it's not prime number.
        2. check num divisble by range of
            - ( 2 , num-1) - not good for long range of num
            - ( 2, square root(num)) - optimised for long range,
                We only check up to √num because any larger factor would have a matching smaller factor.
                eg: num=16 , squareroot of 16 = 4
                    we are checking range(2,4+1) - num is divisible by 2,4
                    so any number multiple of this number can divide num 8,16 etc
'''

#-------------------------------------------Solution 1-----------------------------------------
import math

def check_prime(num):
    if num<2:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True

for i in range(1,100):
    if check_prime(i):
        print(i)

#-------------------------------------------Solution 2-----------------------------------------

def check_prime2():
    for num in range(2,20):
        is_prime = True
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                is_prime = False
                break
        if is_prime:
            print(num)

# print(check_prime2())