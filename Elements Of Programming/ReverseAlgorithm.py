'''
wiggle or zigzag pattern

Input : A = [1, 2, 3, 4, 5, 6]
Output: [1, 3, 2, 5, 4, 6]

 Pattern should follow this rule: A[0]<A[1]>A[2]<A[3]>A[4]<A[5]

'''

def wiggle_pat(arr):
    for i in range(1,len(arr)):
        # Checking the odd index value, if it's less than prev index, swap them.
        if i%2==1:
            if arr[i]<arr[i-1]:
                arr[i],arr[i-1]=arr[i-1],arr[i]
        # Checking the even index value, if it's greater than prev one, swap with prev number.
        else:
            if arr[i]>arr[i-1]:
                arr[i],arr[i-1]=arr[i-1],arr[i]

    return arr

arr = [1, 2, 3, 4, 5, 6]
print(wiggle_pat(arr))