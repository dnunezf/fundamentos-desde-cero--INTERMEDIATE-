# Dates: No es un objeto puro, por eso lo importamos. Es un objeto complejo que utiliza codigo python combinado
# con objetos de tipo basico.

# Importamos modulo datetime; es decir, accedemos a esta caracteristica del core de Python.
# Representa las operaciones y objetos que nos permite trabajar con fechas.
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