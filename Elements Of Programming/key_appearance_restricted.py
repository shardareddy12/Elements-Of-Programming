'''

- compare each number with key
- number is key - and count less that max occcurence replace with i index and increse index i and count
- number is not key - then replace number with array i index and increase the i index
'''

num = [1,2,2,2,3,4,5,5]
key = 2
max_occurence = 2

def restrict_key_occurence(num,key,max_occurence):
    i=0
    count=0
    for j in range(len(num)):
        if num[j]==key:
            if count<max_occurence:
                num[i]=num[j]
                count+=1
                i += 1
        else:
            num[i] = num[j]
            i += 1
    del num[i:]
    return num

print(restrict_key_occurence(num,key,max_occurence))