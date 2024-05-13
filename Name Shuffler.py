# Write a function that returns a string in which firstname is swapped with last name.

# Example(Input --> Output)

# "john McClane" --> "McClane john"

def name_shuffler(str_):
    new_str = str_.split()
    return new_str[-1] + " " + new_str[-2]
