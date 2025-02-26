# in place selection sort

def selection_sort(arr):
    n = len(arr)

    for i in range(0,n):

        min_idx = i
        for j in range(i,n):
            if arr[j]<arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


a = [4,99,3,8,0,444,77777,8,1]
print(a)
b = selection_sort(a)
print(b)




