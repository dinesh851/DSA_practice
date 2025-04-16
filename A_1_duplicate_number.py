# Given an integer array nums, return True if any value appears at least twice in the array,
# and return False if every element is distinct.
# 
# Example:
# Input: nums = [1, 2, 3, 1]
# Output: True
# Explanation: The element 1 appears more than once (at indices 0 and 3).

nums = [1, 2, 3, 1]
nums1 = [1, 2, 3, 4,5]

# method 1 BRUTE FORCE
# using two for loops

def bruteforce(nums):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

# Time Complexity: o(n²) because it uses 2 for loops 
# Space Complexity: O(1) because no extra data stucture is required


# method 2 using sort
# using sorfor loops

def sort(nums):
    nums.sort()
    n = len(nums)
    for i in range(0,n-1):
        if nums[i] == nums[i+1]:
            return True
    return False

# Time Complexity: o(n²) because it uses 2 for loops 
# Space Complexity: O(1) because no extra data stucture is required


# method 3 hash set
# using sets

def sets(nums):
    newset = set()
    for i in nums:
        if i in newset:
            return True
        newset.add(i)
    return False

# Time Complexity: o(n) single for loops 
# Space Complexity: o(n)  because we use set data stucture


# method 4 hash map
# using dictionary / hashmap

def hash_map(nums):
    newhashmap={}
    for i in nums:
        if i in newhashmap:
            return True
        newhashmap[i]=1
    return False

# Time Complexity: o(n) single for loops 
# Space Complexity: o(n)  because we use dictionary/hashmap  data stucture


# Method 6: Using set length comparison

def using_set_length(nums):
    return len(nums) != len(set(nums))

# Time Complexity: O(n) on average (to build the set)
# Space Complexity: O(n) for the set storage



print(bruteforce(nums))
print(bruteforce(nums1))

print(sort(nums))
print(sort(nums1))

print(sets(nums))
print(sets(nums1))

print(hash_map(nums))
print(hash_map(nums1))

print(using_set_length(nums))
print(using_set_length(nums1))