# two sum problem
def two_sum(nums, target):
    num_map = {}  # Hash table to store number and its index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:  # Check if complement is in hash table
            return [num_map[complement], i]  # Return indices
        num_map[num] = i  # Store index of the number in hash table

    return []  # If no solution found

# Example usage
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]
