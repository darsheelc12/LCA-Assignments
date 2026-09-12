# Dictionary Operations

print("--- DICTIONARY OPERATIONS ---")

# Create a dictionary
student = {
    "name": "Darsheel",
    "age": 17,
    "course": "CSE AI-DS"
}

print("Original Dictionary:", student)

# Add a new key-value pair
student["city"] = "Pune"
print("After Adding:", student)

# Update a value
student["age"] = 198
print("After Updating Age:", student)

# Remove an item using pop()
student.pop("city")
print("After Removing City:", student)

# Remove an item using del
del student["age"]
print("After Deleting Age:", student)

# Display all keys
print("Keys:", student.keys())

# Display all values
print("Values:", student.values())


# Tuple Operations

print("--- TUPLE OPERATIONS ---")

# Create a tuple
numbers = (10, 20, 30, 40)

print("Original Tuple:", numbers)

# Add to tuple
# Tuples cannot be directly changed, so we are creating a new tuple.
numbers = numbers + (50,)
print("After Adding:", numbers)

# Removing an element
# Convert tuple to list, remove the element, then convert back
temporary = list(numbers)
temporary.remove(30)
numbers = tuple(temporary)

print("After Removing 30:", numbers)

# Access an element
print("First Element:", numbers[0])

# Find length of tuple 
print("Length of Tuple:", len(numbers))