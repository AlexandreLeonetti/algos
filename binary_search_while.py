def binary_search(arr, target):

    left = 0
    right = len(arr)-1

    while left<right:
        mid = (left + right)//2
        # case arr[mid] == target
        if arr[mid] == target:
            return mid
        # case arr[mid]> target
        if arr[mid] > target:
            right = mid-1

        # case arr[mid]<= target
        if arr[mid] <= target:
           left = mid 


a = [3,4,8,9,11,12,14,22,33,44,45]

print(a)
print(binary_search(a,12))
