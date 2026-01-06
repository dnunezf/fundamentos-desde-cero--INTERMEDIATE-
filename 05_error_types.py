# Error Types: Veremos excepciones comunes en Python. Tipos de errores y cómo manejarlos.

# SyntaxError
#print "Hello, World!" # Uncommenting this line will raise a SyntaxError
print("Hello, World!")  

# NameError
name = "David" # Commenting this line will raise a NameError
print(name)

# IndexError
my_list = ["Python", "Swift", "Kotlin", "JavaScript", "Prolog"]
print(my_list[2])
print(my_list[0])
print(my_list[4])
print(my_list[-1])
#print(my_list[6]) # Uncommenting this line will raise an IndexError  

# ModuleNotFoundError
# import non_existent_module # Uncommenting this line will raise a ModuleNotFoundError
import math

# AttributeError
# print(math.PI) # Uncommenting this line will raise an AttributeError
print(math.pi)

# KeyError
my_dict = {"Nombre":"David", "Apellido":"Nunez", "Edad": 21, 1:"Python"}
# print(my_dict["My_Age"]) # Uncommenting this line will raise a KeyError
print(my_dict["Edad"])

# TypeError
# print(my_list["0"]) # Uncommenting this line will raise a TypeError
print(my_list[0])
print(my_list[False]) # This works because False is equivalent to 0
print(my_list[True]) # This works because True is equivalent to 1

# ImportError
# from math import PI # Uncommenting this line will raise an ImportError
from math import pi
print(pi)

# ValueError
# my_int = int("10 Years") # Uncommenting this line will raise a ValueError
my_int = int("10") # This works fine, converts string "10" to integer 10
print(type(my_int))

# ZeroDivisionError
# print(4/0) # Uncommenting this line will raise a ZeroDivisionError
print(4/2)