# selection sort algo 

def smallest(arr):
    s = arr[0]
    s_idx = 0
    for i in range(len(arr)):
        if arr[i]<s:
            s=arr[i]
            s_idx=i
    return s_idx 

def selection_sort(arr):
    res = []

    for i in range(len(arr)):
        idx = smallest(arr)
        res.append(arr[idx])
        arr.pop(idx)
    return res






a = [99, 2, 90, 8, 9, 33, 0, 777]
print(a)
b = selection_sort(a)
print(b)
