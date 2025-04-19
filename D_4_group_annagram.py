from collections import defaultdict

def group( strs):
    res = defaultdict(list)  # creates a default dictionary where each value is a list
    for s in strs:
        sortedS = ''.join(sorted(s))  # sorts each word to use as a key
        res[sortedS].append(s)        # appends the original word to the correct group
    return list(res.values())         # returns all grouped anagram lists4

strs=["eat", "tea", "tan", "ate", "nat", "bat"]
print(group(strs))
