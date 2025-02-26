 # binary search

def binary_search(arr,n):
    middle = int(len(a)/2)
    # find middle
    # check if middle is bigger than n
    if arr[middle]>=n:
        binary_search([:middle],n)
    # if bigger than n search in smaller half
    if arr[middle]<n:
        binary_search([middle+1:],n)


    # if smaller search in larger half
    # return i when arr[i]==n

a = [2,4,8,34,35,36,88,99,111,123,234,789]

print(a)
print(binary_search(a, 35))
