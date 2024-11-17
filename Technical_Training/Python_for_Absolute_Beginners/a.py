length = int(input("Enter an integer that represents length in feet."))
width = int(input("Enter an integer that represents width in feet."))
height = int(input("Enter an integer that represents height in feet."))
 
 
def prism_vol(l, w, h):
    return l * w * h
 
 
print("The volume of the rectangular prism is " + str(prism_vol(length, width, height)) + " cubic feet.")