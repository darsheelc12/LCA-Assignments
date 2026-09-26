 # checking that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9). 
import re

s = input("Enter the string: ")

if re.fullmatch(r"[a-zA-Z0-9]+", s):
    print("String accepted")
else:
    print("String rejected")
