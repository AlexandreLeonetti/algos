def heapify(arr, n_idx, idx):
    largest_idx = idx  # Initialize largest as root
    left_idx = 2 * idx + 1  # Left child index
    right_idx = 2 * idx + 2  # Right child index

    # Check if left child exists and is greater than root
    if left_idx < n_idx and arr[left_idx] > arr[largest_idx]:
        largest_idx = left_idx

    # Check if right child exists and is greater than the current largest
    if right_idx < n_idx and arr[right_idx] > arr[largest_idx]:
        largest_idx = right_idx

    # If the largest is not root, swap and heapify the affected subtree
    if largest_idx != idx:
        arr[idx], arr[largest_idx] = arr[largest_idx], arr[idx]
        print(arr)
        heapify(arr, n_idx, largest_idx) # call heapify on either right_idx or left_idx if there was a change

    # if largest_idx == idx ( was root) then none of the if statements above are called, and heapify returns.

# Build an array to demonstrate heapify
a = [None] * 9
a[0] = 3
a[1] = 5
a[2] = 4
a[3] = 8
a[4] = 9
a[5] = 6
a[6] = 7
a[7] = 2
a[8] = 1

print("Original array:")
print(a)

# Apply heapify on the subtree rooted at index 0 (entire tree in this case)
heapify(a, len(a), 0)

print("Heapified array:")
print(a)




"""


            3
         /     \
        5       4
       / \     / \
      8   9   6   7
     / \
    2   1




   

            5
         /     \
        3       4
       / \     / \
      8   9   6   7
     / \
    2   1





    

            5
         /     \
        9       4
       / \     / \
      8   3   6   7
     / \
    2   1 
"""