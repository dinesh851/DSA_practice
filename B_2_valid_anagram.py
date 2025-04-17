# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# Example 1:
# Input: s = "racecar", t = "carrace"
# Output: True

# Example 2:
# Input: s = "jar", t = "jam"
# Output: False


# Method 1: Sorting Both Strings

def sort_method(s1,s2):
    if sorted(s1)==sorted(s2):
        return True
    return False

# Time Complexity: O(n log n)
# Space Complexity: O(n)

# Method 2: Using Hash Maps Counting Character Frequency

def counting_char(s1,s2):
    if len(s1) != len(s2) :
        return False
    count_S={}
    count_t={}
    for ch in s1 :
        count_S[ch]=count_S.get(ch,0)+1
    for ch in s2 :
        count_t[ch]=count_t.get(ch,0)+1
    return count_S == count_t

# Time Complexity: O(n)
# Space Complexity: O(1) if only lowercase letters



# Method 3: Using a Single Counter Dictionary
def single_dict(s, t):
    if len(s) != len(t):
        return False

    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1

    for ch in t:
        if ch not in count:
            return False
        count[ch] -= 1
        if count[ch] == 0:
            del count[ch]

    return not count

# Time Complexity: O(n)
# Space Complexity: O(n)


# Method 4: Using collections.Counter
from collections import Counter

def counter_method(s, t):
    return Counter(s) == Counter(t)

# Time Complexity: O(n)
# Space Complexity: O(1)

# Method 5: recursive 

def recursive(s1, s2):
    if len(s1) == 0 and len(s2) == 0:
        return True
    if len(s1) != len(s2):
        return False

    # we are trying to match each letter from s1 with s2/
    # it is recursive type

    for i in range(len(s1)):
        if s1[i] in s2:

            # Removing the letter of s1  if it is already present in s2 
            # : means slicing  in python   example
            # "hello"[:2] = "he"   startingla iruntha before 2 index 0 and 1 index will be displayed
            # "hello"[3:] = "lo"   endingla iruntha  after 3 index 4 and 5 index will be displayed

            remaining_char = s2[:s2.index(s1[i])] + s2[s2.index(s1[i])+1:]

            # Recursively check the rest of the string

            if recursive(s1[:i] + s1[i+1:], remaining_char):
                return True

    return False
# Time Complexity:O(n²)
# Space Complexity: O(n²)

print(sort_method("listen", "silent"))  
print(sort_method("hello", "world"))     


print(counting_char("listen", "silent"))  
print(counting_char("hello", "world"))     

print(single_dict("listen", "silent"))  
print(single_dict("hello", "world"))     

print(counter_method("listen", "silent"))  
print(counter_method("hello", "world"))     

print(recursive("listen", "silent"))  
print(recursive("hello", "world"))     
