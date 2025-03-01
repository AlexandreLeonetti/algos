# binary search while

def binary_search(arr, target):

    left = 0
    right = len(arr)-1

    while left<=right:# the correct condition is left <= right instead of left<right, 
        #in the case of left<right search might terminate before the last possible index
        mid = (left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            right=mid-1
        else :  #arr[mid]< target:
            #if left == mid, left = mid would cause stagnation and left would stop moving indefinitely
            # so we add a +1
            left = mid+1# to ensure progress
    return -1

    


ord_arr = [1,2,3,4,5,5,8,9,12,15,18,22,24]
print(ord_arr)
res = binary_search(ord_arr, 4)
print(res)