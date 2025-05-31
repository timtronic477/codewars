
# Instructions
# Output

# You task is to implement an simple interpreter for the notorious esoteric language HQ9+ that will work for a single character input:

#     If the input is 'H', return 'Hello World!'
#     If the input is 'Q', return the input
#     If the input is '9', return the full lyrics of 99 Bottles of Beer. It should be formatted like this:

# 99 bottles of beer on the wall, 99 bottles of beer.
# Take one down and pass it around, 98 bottles of beer on the wall.
# 98 bottles of beer on the wall, 98 bottles of beer.
# Take one down and pass it around, 97 bottles of beer on the wall.
# 97 bottles of beer on the wall, 97 bottles of beer.
# Take one down and pass it around, 96 bottles of beer on the wall.
# ...
# ...
# ...
# 2 bottles of beer on the wall, 2 bottles of beer.
# Take one down and pass it around, 1 bottle of beer on the wall.
# 1 bottle of beer on the wall, 1 bottle of beer.
# Take one down and pass it around, no more bottles of beer on the wall.
# No more bottles of beer on the wall, no more bottles of beer.
# Go to the store and buy some more, 99 bottles of beer on the wall.

#     For everything else, don't return anything (return null in C#, None in Rust, and "" in Haskell).

# (+ has no visible effects so we can safely ignore it.)

def HQ9(code):
    inp = {
        "H": "Hello World!",
        "Q": code, 
        "9": generate_99_bottles()
    }

    return inp.get(code)


def generate_99_bottles():
    lyrics = []
    for i in range(99, 0, -1):
        next_bottle = f"{i - 1} bottle{'s' if i - 1 != 1 else ''}" if i - 1 > 0 else "no more bottles"
        bottle_str = f"{i} bottle{'s' if i != 1 else ''}"
        lyrics.append(f"{bottle_str} of beer on the wall, {bottle_str} of beer.")
        lyrics.append(f"Take one down and pass it around, {next_bottle} of beer on the wall.")

    lyrics.append("No more bottles of beer on the wall, no more bottles of beer.")
    lyrics.append("Go to the store and buy some more, 99 bottles of beer on the wall.")

    return "\n".join(lyrics)
