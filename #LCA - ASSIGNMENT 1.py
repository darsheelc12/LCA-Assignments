# Dictionary Operations

print("--- DICTIONARY OPERATIONS ---","\n")

# Create a dictionary
student = {
    "name": "Darsheel",
    "age": 17,
    "course": "CSE AI-DS"
}

print("Original Dictionary:", student,"\n")

# Add a new key-value pair
student["city"] = "Pune"
print("After Adding:", student,"\n")

# Update a value
student["age"] = 18
print("After Updating Age:", student,"\n")

# Remove an item using pop()
student.pop("city")
print("After Removing City:", student,"\n")

# Remove an item using del
del student["age"]
print("After Deleting Age:", student,"\n")

# Display all keys
print("Keys:", student.keys(),"\n")

# Display all values
print("Values:", student.values(),"\n")


# Tuple Operations

print("--- TUPLE OPERATIONS ---","\n")

# Create a tuple
numbers = (10, 20, 30, 40)

print("Original Tuple:", numbers,"\n")

# Add to tuple
# Tuples cannot be directly changed, so we are creating a new tuple.
numbers = numbers + (50,)
print("After Adding:", numbers,"\n")

# Removing an element
# Convert tuple to list, remove the element, then convert back
temporary = list(numbers)
temporary.remove(30)
numbers = tuple(temporary)

print("After Removing 30:", numbers,"\n")

# Access an element
print("First Element:", numbers[0],"\n")

# Find length of tuple 
print("Length of Tuple:", len(numbers),"\n")
