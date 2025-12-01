# LAMBDAS: Se entienden como una funcion, pero con una peculiaridad importante: son anonimas, es decir, no tienen nombre.

# mi ejemplo basico de lambda function (equivale a arrow function en JS)
id = lambda x : x
print(id(5))

hola = lambda : "hola"
print(hola())

add = lambda x,y : x+y
print(add(5,10))

# ejemplos curso

# Lambda que suma dos valores. Una lambda posee parametros de entrada. 
# La lambda la almacenamos en una variable 
sum_two_values = lambda first_value, second_value : first_value + second_value
print(sum_two_values(2, 4))

multiply_values = lambda first_value, second_value : first_value * second_value - 3
print(multiply_values(2, 4))

# lambda que pase a estar dentro de una funcion
def sum_three_values(value):
    return lambda first_value, second_value : first_value + second_value + value
print(sum_three_values(5)(2, 4))

# lambda function uses nested if-else logic to classify numbers as Positive, Negative or Zero.
n = lambda x : "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(n(5))
print(n(-3))
print(n(0))