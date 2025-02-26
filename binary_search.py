# binary search algorithms


def binary_search(arr, target, left, right):
    mid = left + (right -left)//2 

    if right < left :
        return -1
    if arr[left] == target:
        return left
    if arr[right] == target:
        return right
    
    if target > arr[mid]:
        return binary_search(arr, target, mid+1, right)
    
    if target <= arr[mid]:
        return binary_search(arr, target, left, mid)





a = [2,2,2,5,5,8,11,13,15,22,33,55]
idx = binary_search(a, 13, 0, len(a)-1)
print(a)
print(idx)
