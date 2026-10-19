
# 1. CREATE AND WRITE DATA INTO A FILE

with open("student.txt", "w") as file:
    file.write("Name: Sandeep\n")
    file.write("Course: CSE AI & ML\n")
    file.write("Age: 22\n")

print("Data written successfully!")


# 2. READ DATA FROM A FILE

with open("student.txt", "r") as file:
    data = file.read()

print("\nStudent Details:")
print(data)


# 3. APPEND NEW DATA TO AN EXISTING FILE

with open("student.txt", "a") as file:
    file.write("College: Sandip University\n")

print("New data added successfully!")


# 4. READ THE UPDATED FILE

with open("student.txt", "r") as file:
    data = file.read()

print("\nUpdated Student Details:")
print(data)


# 5. CREATE A NEW FILE USING 'x' MODE

with open("newfile.txt", "x") as file:
    file.write("This is a new file.")

print("New file created successfully!")


# 6. READ A FILE LINE BY LINE

with open("student.txt", "r") as file:
    for line in file:
        print(line, end="")


# 7. CHECK WHETHER A FILE EXISTS

import os

if os.path.exists("student.txt"):
    print("\nThe file exists.")
else:
    print("\nThe file does not exist.")


# 8. DELETE A FILE (OPTIONAL)

# Uncomment these lines only if you want to delete the file.
# if os.path.exists("newfile.txt"):
#     os.remove("newfile.txt")
#     print("File deleted successfully.")
