from functools import reduce

# HIGHER ORDER FUNCTIONS: Funciones que hacen cosas con funciones dentro. Son los ciudadanos de primer orden (lo mas alto de la jerarquia).
# Funciones dentro de funciones

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

# Esto refleja aue aprovechamos la logica de esta funcion, pero al tratarse de una funcion de orden superior, somos capaces de enviarle una funcion que haga lo que se necesite.
# Pasamos funciones que ya tenemos definidas
def sum_two_values_and_add_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)
# Hemos decidido utilizar una funcion que hace una cosa, y luego otra que hace otra cosa; pero siempre reutilizando la logica de la funcion principal.
print(sum_two_values_and_add_value(5, 2, sum_one))
print(sum_two_values_and_add_value(5, 2, sum_five))

# CLOSURES: Concepto de funcion que recibe una funcion y retorna una funcion.

# Definicion de una funcion dentro de otra funcion.
# Retorna la funcion interna.
def sum_ten():
    def add(value):
        return value + 10
    return add

add_closure = sum_ten()
print(add_closure(5))

# Se guarda todo el contexto (original_value). 
def sum_two(original_value):
    def add(value):
        return value + 2 + original_value
    return add

add_closure = sum_two(1)
print(add_closure(5))
print(sum_two(3)(5)) # concatenamos llamadas a las funciones

# Built-in higher order functions: map, filter, reduce

# MAP: necesita un conjunto iterable y una funcion para aplicar a cada uno de los elementos.
# multiplica por 2 cada uno de los elementos de numbers
numbers = [2, 4, 8, 16, 32, 64, 128, 256]

def multiply_by_two(number):
    return number * 2
print(list(map(multiply_by_two, numbers)))
print(list(map(lambda number : number * 2, numbers))) # version con lambda function, sin utilizar multiply_by_two

# MAP con lambda function
a = [1, 2, 3, 4, 5]
b = map(lambda x : x * 2, a)
print(list(b))

# FILTER: necesita un conjunto iterable y una funcion que devuelva True o False para cada uno de los elementos.
numbers = [1, 2, 5, 10, 15, 20, 25, 30, 35, 40]

def filter_greater_than_ten(number):
    return number > 10
print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number : number > 10, numbers))) # version con lambda function, sin utilizar filter_greater_than_ten

# FILTER con lambda function
n = [1, 2, 3, 4, 5, 6]
even = filter(lambda x : x % 2 == 0, n)
odd = filter(lambda x : x % 2 != 0, n)
print(list(even))
print(list(odd))

# REDUCE: necesita un conjunto iterable y una funcion que reciba dos parametros. Se aplica la funcion de forma acumulativa a los elementos del iterable.
# NOTA: reduce no es una funcion built-in, hay que importarla desde functools

numbers = [1, 2, 5, 10, 15, 20, 25, 30, 35, 40]

# suma todos los elementos de la lista. Suma el primer elemento más el acumulado, y así sucesivamente.
def sum_two_values(first_value, second_value):
    return first_value + second_value
# No tenemos como resultado una lista, sino un unico valor.
print(reduce(sum_two_values, numbers))

# REDUCE con lambda function
a = [1, 2, 3, 4, 5]
b = reduce(lambda x, y : x + y, a)
print(b)