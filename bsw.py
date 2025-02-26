


def bsw(arr, target):
    left, right = 0, len(arr)-1

    while left<right:
        mid = (left + right)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid-1
        else:
            left = mid



a=[3,4,5,6,8,9,11,13,14,15,22,33,44,55]
print(a)
print(bsw(a,13))

