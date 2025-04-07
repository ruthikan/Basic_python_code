#1Write a function called calculate_area that takes base and height as an input and 
#returns and area of a triangle. Equation of an area of a triangle is,
#area = (1/2)*base*height

def calculate_area():
    base=int(input("enter the base of the triangle:"))
    height=int(input("enter the height of the triangle:"))
    area=0.5*base*height
    print("area of triangle is:",area)
calculate_area()

#2.Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle".
#  Based on shape type it will calculate area. 
#If no shape is supplied then it should take triangle as a default shape

def calculate_area(d1,d2,shape='triangle'):
    if shape=='triangle':
        area=0.5*d1*d2
        print("area of traingle:",area)
    elif shape=='rectangle':
        area=d1*d2
        print("area of reactangle:",area)
    else:
        print("Error: Input shape is neither triangle nor rectangle.")
        area=None
    return area
calculate_area(d1=45,d2=89)
calculate_area(d1=78,d2=57,shape="rectangle")

#3.# 3. Write a function called print_pattern that takes integer number as an argument and 
# prints following pattern if input number is 3,
# ```
# *
# **
# ***
# ```
# if input is 4 then it should print
# ```
# *
# **
# ***
# ****
# ```
# Basically number of lines it prints is equal to that number.

def print_pattern(n):
     for i in range(n):
        s = ''
        for j in range(i+1):
            s = s + '*'
        print(s)
n=int(input("enter the input number for pattern"))
print_pattern(n)
