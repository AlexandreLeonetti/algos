def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than the current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest is not root, swap and heapify the affected subtree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        print(arr)
        heapify(arr, n, largest)



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