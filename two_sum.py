# two sum
def two_sum(nums, target):
    num_map = {}  # Dictionary to store numbers and their indices

    for i, num in enumerate(nums):
        complement = target - num  # What we need to find

        if complement in num_map:
            return [num_map[complement], i]  # Return indices of the two numbers

        num_map[num] = i  # Store the current number with its index

    return []  # No solution found

# Example usage
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print("Indices:", result)  # Expected Output: [0, 1]
