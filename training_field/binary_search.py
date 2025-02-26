


def bin_search(a, target):
    # define left and right search intervals
    left=0
    right=len(a)-1
    mid = (left+right)//2
    # define mid (truncated)

    while left<right:
        if a[mid]==target:
            return mid
        if a[mid]<target:
            right=mid-1
        else:
            left=mid
        mid = (left+right)//2

    return -1

arr = [0,2,4,6,8,11,12,13,15,18,20]

x = bin_search(arr, 101)
print(arr)
print(x)


