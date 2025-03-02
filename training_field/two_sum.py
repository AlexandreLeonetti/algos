# two sum problem


def two_sum(arr, target):
    #
    hash1 = {}
    for i, a in enumerate(arr):
        complement = target - a
        if complement in hash1:
            return (i, hash1[target-a])
        hash1[a]=i

    return -1



# usage
# two sum returns a couple of indexes representing the digits to be added to reach target


a1 = [3,3,2,7,5,8,10]
print(a1)
print(two_sum(a1,6))