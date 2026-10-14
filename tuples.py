# 1. Creating a tuple
fruits = ("Apple", "Banana", "Mango", "Orange", "Banana")

print("Original tuple:", fruits)

# 2. Accessing tuple items
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# 3. Slicing a tuple
print("First three fruits:", fruits[0:3])

# 4. Finding the length
print("Total items:", len(fruits))

# 5. Checking whether an item exists
print("Is Mango present?", "Mango" in fruits)

# 6. Counting duplicate items
print("Banana count:", fruits.count("Banana"))

# 7. Finding the index of an item
print("Index of Mango:", fruits.index("Mango"))

# 8. Looping through a tuple
print("All fruits:")
for fruit in fruits:
    print(fruit)

# 9. Tuple with different data types
student = ("Sandeep", 22, "CSE", 7.62)
print("Student details:", student)

# 10. Single-item tuple
single = (10,)
print("Single-item tuple:", single)

# 11. Joining two tuples
a = (10, 20, 30)
b = (40, 50, 60)
combined = a + b
print("Combined tuple:", combined)

# 12. Repeating a tuple
print("Repeated tuple:", a * 2)

# 13. Checking the tuple type
print("Data type:", type(fruits))

# 14. Tuple unpacking
name, age, branch, cgpa = student
print("Name:", name)
print("Age:", age)
print("Branch:", branch)
print("CGPA:", cgpa)

# 15. Immutability: tuples cannot be changed
# fruits[0] = "Grapes"
# Uncomment the line above to see a TypeError.

# 16. Converting a list into a tuple
numbers_list = [1, 2, 3, 4]
numbers_tuple = tuple(numbers_list)
print("List converted to tuple:", numbers_tuple)

# 17. Converting a tuple into a list
new_list = list(numbers_tuple)
print("Tuple converted to list:", new_list)