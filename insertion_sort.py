# insertion sort :def insertion_sort(arr):
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Element to be placed correctly
        j = i - 1

        # Shift elements of the sorted part of the array
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insert the key at its correct position
        arr[j + 1] = key

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
insertion_sort(arr)
print("Sorted Array:", arr)



