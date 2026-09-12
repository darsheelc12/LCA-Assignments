#LCA - ASSIGNMENT 2
#TO FIND LARGEST OF THREE NUMBERS

num1=int(input("enter your first number : "))
num2=int(input("enter your second number : "))
num3=int(input("enter your third number : "))

if num1>num2 and num1>num3 :
    print("number 1 is largest")
elif num2>num3 :
    print("number 2 is largest")
else :
    print("number 3 is largest")