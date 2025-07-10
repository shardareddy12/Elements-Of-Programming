'''
Input :
a=[a,b,c,d] and p=[2,0,1,3]

Output:
[b,c,a,d]

- a is your array of elements: positions 0 → a, 1 → b, 2 → c, 3 → d.
- p is a permutation array (or sometimes called a permutation mapping), meaning:
  “where should each element go?”
- Element at position i in a should be moved to position p[i] in the result.

- There are two solutions using extra space and other one without using extra space

'''

#-----------------------Solution 1-----------------------

a=["a","b","c","d"]
p=[2,0,1,3]

res = [None]* len(a)   # one arr where length is same as "a" and all elements should be none

def permutation_arr(a,p):
    for i in range(0,len(a)):
        idx = p[i]
        res[idx] = a[i]
    return res


#-----------------------Solution 2 ------------------------

''' 
In-place - without using extra space
'''

def permut_arr(a,p):
    n= len(a)
    for i in range(n):
        while p[i]!=i: # if index is same as p's index we don't have to change the element
            target = p[i]
            a[i], a[target] = a[target], a[i]    # Swap a[i] with a[target]
            p[i], p[target] = p[target], p[i]    # Swap p[i] with p[target] to keep track
    return a

print("sol2 res",permut_arr(a,p))
