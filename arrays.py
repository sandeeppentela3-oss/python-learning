import array

# Creating an array
numbers = array.array('i', [10, 20, 30, 40, 50])

# Printing the array
print(numbers)

# Accessing elements
print(numbers[0])
print(numbers[2])


import array

numbers = array.array('i', [10, 20, 30])

# Add an element
numbers.append(40)
print(numbers)

# Insert an element at index 1
numbers.insert(1, 15)
print(numbers)

# Remove an element
numbers.remove(30)
print(numbers)

# Access an element
print(numbers[0])

# Find the length
print(len(numbers))


import array

a = array.array('i', [10, 20, 30, 40])

print(a)
print(a[0])



import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

print(a)
print(a[1][2])


import numpy as np

a = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print(a)
print(a[1][0][1])