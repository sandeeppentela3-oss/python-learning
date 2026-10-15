
# Python Strings

# 1. Creating strings
name = "Sandeep"
language = 'Python'
message = """Welcome to Python programming"""

print("Name:", name)
print("Language:", language)
print("Message:", message)

# 2. Finding the length
print("Length:", len(name))

# 3. Uppercase and lowercase
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())

# 4. Concatenation (joining strings)
first = "Hello"
second = "World"
print("Concatenation:", first + " " + second)

# 5. Repetition
print("Repetition:", "Hi " * 3)

# 6. Indexing
word = "Python"
print("First character:", word[0])
print("Last character:", word[-1])

# 7. Slicing
print("First three characters:", word[0:3])
print("From index 2:", word[2:])

# 8. Replacing text
print("Replace:", word.replace("Python", "Java"))

# 9. Checking whether text exists
print("Is 'th' present?", "th" in word)

# 10. Removing extra spaces
text = "  Hello Python  "
print("Stripped:", text.strip())

# 11. String formatting
age = 22
print(f"My name is {name} and I am {age} years old.")

# 12. Taking string input
user_name = input("Enter your name: ")
print(f"Hello, {user_name}!")
