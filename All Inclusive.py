# Input:

#     a string strng
#     an array of strings arr

# Output of function contain_all_rots(strng, arr) (or containAllRots or contain-all-rots):

#     a boolean true if all rotations of strng are included in arr
#     false otherwise

# Examples:

# contain_all_rots(
#   "bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"]) -> true

# contain_all_rots(
#   "Ajylvpy", ["Ajylvpy", "ylvpyAj", "jylvpyA", "lvpyAjy", "pyAjylv", "vpyAjyl", "ipywee"]) -> false)

# Note:

# Though not correct in a mathematical sense

#     we will consider that there are no rotations of strng == ""
#     and for any array arr: contain_all_rots("", arr) --> true

def contain_all_rots(s, arr):
    rotations = [s[i:] + s[:i] for i in range(len(s))]
    return all(r in arr for r in rotations)
