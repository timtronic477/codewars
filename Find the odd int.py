# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.
# Examples

# [7] should return 7, because it occurs 1 time (which is odd).
# [0] should return 0, because it occurs 1 time (which is odd).
# [1,1,2] should return 2, because it occurs 1 time (which is odd).
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

def find_it(seq):
    count = {}
# create dictionary to count number of times its used
    for i in seq:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
# loop through keys and values to see what is odd and return the key
    for key, value in count.items():
        if value % 2 == 1:
            return key
        else:
            pass


# top solution 

def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
