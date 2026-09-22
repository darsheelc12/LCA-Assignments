s = input("Enter the string: ")

valid = True

for char in s:
    if char.isalpha() or char.isdigit():
        valid = True
    else:
        valid = False
        break

if valid:
    print("String accepted")
else:
    print("String rejected")