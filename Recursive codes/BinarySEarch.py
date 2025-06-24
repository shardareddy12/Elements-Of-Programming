


def binary_serach(arr,searchNo,low,high):
    mid = int((low + high)/2)
    if low>high:
        return False
    elif searchNo==arr[mid]:
        print("element present at index",mid)
        return arr[mid]
    else:
        if searchNo>arr[mid]:
            low=mid+1
            return binary_serach(arr,searchNo,low,high)
        else:
            high=mid-1
            return binary_serach(arr,searchNo,low,high)

arr=[2,4,7,9,10,11,12,16,18,20]
searchNo=12
print(binary_serach(arr,searchNo,0,len(arr)))



