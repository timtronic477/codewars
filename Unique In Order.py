# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

# For example:

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
# unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]


def unique_in_order(sequence):
    arr = []
    if sequence == "" or sequence == [] or sequence ==():
        return []
    elif len(sequence) == 1:
        return list(set(sequence))
    elif len(sequence) == 2:
        if sequence[0] == sequence[1]:
            arr.append(sequence[0])
            return arr
        else:
            return arr.append(sequence[0])
    # return list where the previous value doesn't equal the current value
    else:
        arr.append(sequence[0])
        for i in range(1, len(sequence)):
            if sequence[i] != sequence[i - 1]:
                arr.append(sequence[i])
        return arr


# top solution

def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result
