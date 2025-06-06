# Implement a function that returns the minimal and the maximal value of a list (in this order).

def get_min_max(seq): 
    return (sorted(seq)[0], sorted(seq)[len(seq)-1])
