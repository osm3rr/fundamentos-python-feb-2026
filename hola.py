# Variables en python
from tkinter.font import names


name = "Ruperto" # string
#age = 30 # integer
height = 1.75 # float   
is_student = True # boolean


# malas practicas
x = 10
Name = "Juan"
#name-last_name = "Perez"
#number.first = 5
AGE = 25
PI = 3.14

# operadores matematicos basicos
number1 = 10
number2 = 5

# suma
result_sum = number1 + number2
# print(result_sum)

# print("El resultado de la suma es:", result_sum)

# print(f"El resultado de la suma es: {result_sum}")

# resta
result_subtraction = number1 - number2
# print(f"El resultado de la resta es: {result_subtraction}")

# multiplicacion
result_multiplication = number1 * number2
# print(f"El resultado de la multiplicacion es: {result_multiplication}")

# division
result_division = number1 / number2
# print(f"El resultado de la division es: {result_division}") 

# modulo o residuo
result_modulo = number1 % number2
# print(f"El resultado del modulo es: {result_modulo}")

# Operadores de comparacion
# mayor que >
# menor que <
# igual a ==
# diferente de !=
# mayor o igual que >=
# menor o igual que <=


# condicional simple
# age = 17
# if age >= 18:
#     print("Eres mayor de edad")
# else:
#     print("Eres menor de edad")

# Condicional anidado
# age = 16
# weekday = "Jueves"

# if age >= 18:
#     if weekday == "Viernes":
#         print("Eres mayor de edad y es viernes")
#     else:
#         print("Eres mayor de edad pero no es viernes")
# else:
#     print("Eres menor de edad")

# # condicionales en cadena
# age = 19
# weekday = "Lunes"

# if age >= 18:
#     if weekday == "Viernes":
#         print("Eres mayor de edad y es viernes")
#     elif weekday == "Sábado":
#         print("Eres mayor de edad y es sábado")
#     elif weekday == "Domingo":
#         print("Eres mayor de edad y es domingo")
#     else:
#         print("Eres mayor de edad pero no es fin de semana")
# else:
#     print("Eres menor de edad")

# Operadores logicos
# age = 19
# weekday = "Lunes"

# if (age >= 18) and ((weekday == "Viernes") or (weekday == "Sábado")):
#         print("Eres mayor de edad y es viernes o sábado")
# else:
#     print("Eres menor de edad y no es viernes ni sábado")

# # estructuras de datos
# # cadena de texto
# greeting = "Hola, ¿cómo estás?"
# number1 = 10
# number_float = 3.14
# is_raining = False  

# # lista
# fruits = ["manzana", "banana", "naranja", 10, 3.14, True]

# names_list = [
#     "Juan",
#     "María",
#     "Pedro"
#     ]

# # methods de lista
# # names.pop()

# # add a new name to the list
# names_list.append("Ana")
# print(names_list[-1])

# names_list[0]= "Carlos"
# print(names_list[0])

# # tupla
# coordinates = (10.0, 20.0, 30.0)

# print(coordinates[0])

# names[0] = "Carlos"
# print(names[0])

# coordinates[0] = 15.0
# print(coordinates[0])

# diccionario
# person = {
#     "name": "Juan",
#     "age": 30,
#     "height": 1.75,
#     "is_student": True,
#     "grades": [8, 9, 10]
# }

# print(person["height"])


# Ciclo for
# name list
names = ["Juan", "María", "Pedro"]

# for name in names:
#     print(name)

# print(len(names))

# for name in range(len(names)):
#     print(names[name])

# functions in python

# def greet():
#     print("Hola, ¿cómo estás?")

# greet()

# def greet(name):
#     print(f"Hola {name}, ¿cómo estás?")

# greet("Ruperto")

# suma de dos numeros
# def sum_numbers(num1, num2):
#     result = num1 + num2
#     return result

# print(sum_numbers(5, 10))

# resta de dos numeros
def subtract_numbers(num1:int, num2:int) -> int:
    """
    Esta función recibe dos números y devuelve la resta de ambos.
    Args:
        num1 (int): El primer número.
        num2 (int): El segundo número.
    Returns:
        int: La resta de num1 y num2.
    """
    result = num1 - num2
    return result

print(subtract_numbers(num2=5, num1=10))

