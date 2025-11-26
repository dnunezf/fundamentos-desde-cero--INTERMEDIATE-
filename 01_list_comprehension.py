# List Comprehension: Forma de crear listas comprimidas. Formato concreto para crear listas de forma rapida, con 
# base a listas que ya tenemos.
# Nos vale para crear una lista que nosotros ya estamos operando sobre ella en el momento en que la vamos a definir.

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list)

# creamos una nueva lista, aplicando list comprehension. Forma mas rapida de crear listas
my_list = [i for i in my_original_list]
print(my_list)

my_list = [i for i in range(8)]
print(my_list)

my_list = [i+1 for i in range(8)]
print(my_list)

my_list = [i*2 for i in range(8)]
print(my_list)

my_list = [i*i for i in range(8)]
print(my_list)

# creamos una lista con un rango de valores
my_range = range(8)
print(list(my_range))

# usamos una funcion para operar sobre los valores de la lista
def sum_five(number):
    return number + 5

my_list = [sum_five(i) for i in range(8)]
print(my_list)