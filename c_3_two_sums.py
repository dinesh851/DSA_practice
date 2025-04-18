



# method 1 BRUTE FORCE
# using two for loops

def twoSum( nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

nums = [3,4,5,6]
target = 7
print(twoSum(nums,target))
# Time Complexity: o(n²) because it uses 2 for loops 
# Space Complexity: O(1) because no extra data stucture is required

