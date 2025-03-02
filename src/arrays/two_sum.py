# two sum problem
# given an array and a target return the two indexes that form the target number


def two_sum(arr, target):
    seen={}# hash table
    for i, a in enumerate(arr):
        complement = target-a
        if complement in seen:
            return (i, seen[complement])
        seen[a]=i
        
#Input: 
nums = [2,7,11,15] 
target = 9
#Output: [0,1]  # nums[0] + nums[1] = 2 + 7 = 9
print(nums)
print(two_sum(nums, target))
