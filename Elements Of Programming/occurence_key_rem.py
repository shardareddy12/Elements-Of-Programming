
'''
Same as duplicate delete- but here we want to delete key from array
- compare each number with key
- number is not key - then replace number with array i index and increase the i index 
'''
num=[1,2,2,3,4,5,5]
key=2
def occure_rem(num,key):
    i=0
    for j in range(len(num)):
        if num[j]!=key:
            num[i]=num[j]
            i+=1
    return num[:i]

print(occure_rem(num,key))