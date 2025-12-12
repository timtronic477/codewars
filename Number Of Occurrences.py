# Write a function that returns the number of occurrences of an element in an array.
# Examples

# sample = [0, 1, 2, 2, 3]
# number_of_occurrences(0, sample) == 1
# number_of_occurrences(4, sample) == 0
# number_of_occurrences(2, sample) == 2
# number_of_occurrences(3, sample) == 1

def number_of_occurrences(element, sample):
    h = {}
    for i in sample:
        if i not in h: 
            h[i] = 1
        else:
            h[i] += 1
    return h[element] if element in h else 0
