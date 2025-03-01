# let's write a function that heapify a subtree
# and then apply this heapify function to a whole array in a bottom up fashion



def heapify( arr, n, root_idx): # takes array, length of array and root node
    # define max element, left and right children as this function moves from root to leaves
    largest_idx = root_idx
    left_idx = root_idx*2 + 1
    right_idx = root_idx*2 + 2

    if left_idx < n and arr[left_idx]> arr[largest_idx]:
        largest_idx= left_idx
    
    if right_idx < n and arr[right_idx] > arr[largest_idx]:
        largest_idx= right_idx

    if root_idx != largest_idx:
        arr[root_idx], arr[largest_idx] = arr[largest_idx], arr[root_idx] 
        heapify(arr, n, largest_idx)




arr = [3, 9, 2, 1, 4, 5]
print(arr)
n=len(arr)


heapify(arr,len(arr)-1,0)
print(arr)

print(range(0,10))
for i in range(len(arr)//2-1,-1, -1):
    print(i)
    heapify(arr, len(arr)-1, i)

print(arr)
print("range(0,10)")
for i in range(0,10):
    print(i)

print("range(10,0,-1)")
for i in range(10,0,-1):
    print(i)
# range( start included, end excluded, step)
