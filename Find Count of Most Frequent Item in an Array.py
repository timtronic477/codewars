# Complete the function to find the count of the most frequent item of an array. You can assume that input is an array of integers. For an empty array return 0
# Example

# input array: [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]
# ouptut: 5 

# The most frequent number in the array is -1 and it occurs 5 times.
# Complete the function to find the count of the most frequent item of an array. You can assume that input is an array of integers. For an empty array return 0
# Example

# input array: [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]
# ouptut: 5 

# The most frequent number in the array is -1 and it occurs 5 times.

def most_frequent_item_count(collection):
    x = {}
    for i in collection:
        if str(i) in x:
            x[str(i)] += 1
        else:
            x[str(i)] = 1
    return max(x.values()) if len(collection) > 0 else 0
