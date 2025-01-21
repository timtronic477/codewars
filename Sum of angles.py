# Find the total sum of internal angles (in degrees) in an n-sided simple polygon. N will be greater than 2.

def angle(n):
    return int(((n-2)*180/n) *n)
