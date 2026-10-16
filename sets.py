
# Creating sets
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Set A:", a)
print("Set B:", b)

# Adding an element
a.add(10)
print("After adding:", a)

# Removing an element
a.remove(10)
print("After removing:", a)

# Union
print("Union:", a | b)

# Intersection
print("Intersection:", a & b)

# Difference
print("Difference:", a - b)

# Symmetric difference
print("Symmetric difference:", a ^ b)

# Checking membership
print("Is 2 in A?", 2 in a)

# Number of elements
print("Length of A:", len(a))
