# Given a list of digits, return the smallest number that could be formed from these digits, using the digits only once (ignore duplicates).

# Notes:
# Only positive integers will be passed to the function (> 0 ), no negatives or zeros.
# Input >> Output Examples
# minValue ({1, 3, 1})  ==> return (13)

def min_value(digits):
    return int(''.join([str(element) for element in sorted(set(digits))]))
