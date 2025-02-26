# heapify function from memory



def heapify( arr, n_idx, root_idx):
    # define largest_idx, left and right children indexes

    largest_idx = root_idx
    left_idx = 2*root_idx + 1
    right_idx = 2*root_idx + 2


    # if left_idx exist and bigger than root_idx then largest is left
    if left_idx < n_idx and arr[left_idx]>arr[largest_idx]:
        largest_idx = left_idx

    if right_idx < n_idx and arr[right_idx]>arr[largest_idx]: # if right is even bigger than left, idx will be set to right else nothing happens, 
        # so biggest children is swapped with root of tree
        largest_idx = right_idx
    
    # if any of the if statements have been validated it means the largest_idx is no longer root
    if largest_idx!=root_idx:
        arr[largest_idx], arr[root_idx]= arr[root_idx], arr[largest_idx]
        heapify(arr, n_idx, largest_idx) #" the new root is which ever left or right got swapped"
    
    # else nothing happened, subtree was valid,  no further check.
    # because function assumes other subtrees are valid already
    # the function moves in top to down order



arr = [3, 9, 2, 1, 4, 5]
print(arr)
n=len(arr)

start = n//2 -1
# last nont leaf node is n//2 -1
end_not_included = -1 # last index of the array i guess
step = -1 # moving backward

for i in range(start, end_not_included, step):
    heapify(arr, len(arr), i)

print(arr) # arr is heapified

for i in range(n-1, 0, -1):
    arr[i],arr[0]=arr[0],arr[i]
    heapify(arr, i, 0)

print(arr)
# at first glance, building a full heap is nlogn
# but mathematically it is actually just n because moset nodes are closer to bottom so time to heapify heac time is just one
# that is O(h) where hmax is log n and most h will just be 1

# so entire heapify process of array is just O(n)

# we swap biggest element n times so there is a n factor
# we heapify a single element from top to bottom each time, with heighe of log n
# so the sorting process is O(n*logn)  


# the total is O(n) + O(nlogn) so total is O(nlogn) ( the maximum power term in the sum)
# this sums up the heap sort algorithm



