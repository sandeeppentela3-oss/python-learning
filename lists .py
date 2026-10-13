

# 1. Creating a list
fruits = ["Apple", "Banana", "Mango"]
print("Original list:", fruits)

# 2. List with different data types
data = [10, "Python", 25.5, True]
print("Different data types:", data)

# 3. Accessing list items (indexing)
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])
print("Last fruit:", fruits[-1])

# 4. List slicing
print("First two fruits:", fruits[0:2])
print("All fruits:", fruits[:])

# 5. Changing an item
fruits[1] = "Orange"
print("After changing:", fruits)

# 6. Adding items using append()
fruits.append("Grapes")
print("After append:", fruits)

# 7. Inserting an item using insert()
fruits.insert(1, "Banana")
print("After insert:", fruits)

# 8. Adding multiple items using extend()
fruits.extend(["Pineapple", "Guava"])
print("After extend:", fruits)

# 9. Removing an item using remove()
fruits.remove("Orange")
print("After remove:", fruits)

# 10. Removing an item using pop()
removed_item = fruits.pop()
print("Popped item:", removed_item)
print("After pop:", fruits)

# 11. Deleting an item using del
del fruits[0]
print("After del:", fruits)

# 12. Finding the length of a list
print("Length of fruits:", len(fruits))

# 13. Checking whether an item exists
print("Is Mango present?", "Mango" in fruits)

# 14. Counting duplicate values
numbers = [10, 20, 10, 30, 10]
print("Count of 10:", numbers.count(10))

# 15. Finding an item's index
print("Index of 20:", numbers.index(20))

# 16. Sorting a list
numbers.sort()
print("Ascending order:", numbers)

numbers.sort(reverse=True)
print("Descending order:", numbers)

# 17. Reversing a list
numbers.reverse()
print("Reversed list:", numbers)

# 18. Copying a list
original = [1, 2, 3]
copied = original.copy()
print("Copied list:", copied)

# 19. Looping through a list
languages = ["Python", "Java", "C++"]
print("Programming languages:")
for language in languages:
    print(language)

# 20. Looping using range() and indexing
for i in range(len(languages)):
    print("Index:", i, "Value:", languages[i])

# 21. List comprehension
squares = [x * x for x in range(1, 6)]
print("Squares:", squares)

# 22. Filtering items using list comprehension
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print("Even numbers:", even_numbers)

# 23. Nested list
matrix = [[1, 2], [3, 4], [5, 6]]
print("Nested list:", matrix)
print("Element at row 1, column 2:", matrix[0][1])

# 24. Joining two lists using +
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print("Combined list:", combined)

# 25. Repeating a list using *
print("Repeated list:", [1, 2] * 3)

# 26. Finding minimum, maximum and sum
values = [10, 20, 30, 40]
print("Minimum:", min(values))
print("Maximum:", max(values))
print("Sum:", sum(values))

# 27. Clearing all items
temporary = [1, 2, 3]
temporary.clear()
print("After clear:", temporary)