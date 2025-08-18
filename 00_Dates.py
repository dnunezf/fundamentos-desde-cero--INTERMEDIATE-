# Dates: No es un objeto puro, por eso lo importamos. Es un objeto complejo que utiliza codigo python combinado
# con objetos de tipo basico.

# Importamos modulo datetime; es decir, accedemos a esta caracteristica del core de Python.
# Representa las operaciones y objetos que nos permite trabajar con fechas y/o tiempo.
from datetime import datetime 

now = datetime.now() # Obtenemos la fecha y hora actual del sistema.

def print_date(date):
    print(date.year) 
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)

    # DESDE 1970. A partir de un timestamp, podemos inferir una fecha. Formato estandar, cuando trabajamos en BD
    # utilizamos timestamp.
    print(date.timestamp())

print_date(now)

# Definir y trabajar con una fecha, con base a unos datos. Por defecto, se requiere year, month, day
year_2025 = datetime(2025, 1, 1)

print_date(year_2025)

# Representa tiempo
from datetime import time

# current_time = time() # Objeto que no tiene nada, debemos lanzar operaciones para acceder a sus datos. Encapsula tiempo
# No lo podemos inicializar con base a la fecha del sistema
current_time = time(21, 6, 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

# Representa fecha
from datetime import date

# current_date = date() # Debemos definir el objeto
current_date = date.today() # Debemos definir el objeto

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2022, 10, 6)

print(current_date.year)
print(current_date.month)
print(current_date.day)

# Operacion con fechas
current_date = date(current_date.year, current_date.month + 1, current_date.day)

print(current_date.month)

diff = year_2025 - now  # Diferencia entre dos fechas, tipo datetime
print(diff)
diff = year_2025.date() - current_date  # Diferencia entre dos fechas, tipo date
print(diff)

# con time no podemos operar entre tiempos

# Operar con distintas fechas
from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 50, 50, weeks=13)
print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
print(end_timedelta / start_timedelta)