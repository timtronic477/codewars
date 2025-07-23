# Reverse every other word in a given string, then return the string. Throw away any leading or trailing whitespace, while ensuring there is exactly one space between each word. Punctuation marks should be treated as if they are a part of the word in this kata.

def reverse_alternate(st):
    arr = list(filter(lambda i: i != "", st.strip().split(" ")))
    f = []
    for i in range(0, len(arr)):
        if i%2 == 1:
            f.append("".join(reversed(arr[i])))
        else:
            f.append(arr[i])
    return " ".join(f)
