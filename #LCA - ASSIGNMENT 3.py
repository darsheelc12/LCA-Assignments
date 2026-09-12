#LCA - ASSIGNMENT 3
#TO CHECK WHETHER OR NOT THE TRIANGLE IS RIGHT ANGLED TRIANGLE USING FUNCTION 

def check_rightangledtriangle_(side1,side2,side3): 
    if side1**2 + side2**2 == side3**2 :
        return "it is a right angled triangle "
    else:
        return "it is not a right angled triangle "
side1 = int(input("enter your side 1 :"))
side2 = int(input("enter your side 2 :"))
side3= int(input("enter your side 3 :"))

print(check_rightangledtriangle_(side1,side2,side3))


