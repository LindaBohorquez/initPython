#from typing import Text


#print("¿cuantas horas trabjas?")
#quantity1 = input()
#print("¿cuanto cuesta una hora?")
#quantity2 = input()
#print("su valor diario es", int(quantity1) * int(quantity2), "pesos diarios")
#
#print("hello")
#print("escribe una palabra")
#Text1 = input()
#print(Text1.upper())
#print("escribe una palabra")
#text2 = input()
#print(text2.lower())

"""age = input("write your age ")
datatype = type(age)
print(age)
print(datatype)"""


#PRIMER EJERCICIO FOR 
#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

"""word = input("introduce una palabra ")
for i in range(3):
    print(word)"""

#SEGUNDO EJERCICIO FOR
#Escribir un programa que pregunte al usuario su edad  
#muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

"""age = int(input("¿Cuántos años tienes? "))             #DUDA: por que str? pq no puede concatenar int con str
for i in range(age):
    print("Has cumplido " + str(i+1) + " años")
"""
#TERCER EJERCICIO FOR
#Escribir un programa que pida al usuario un número entero positivo 
#muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas

"""n = int(input("Introduce un número entero positivo: "))
for i in range(2, n+1, 2):                                 #aqui esta en par
    print(i, end=", ")

#si inicio con impar da impar
#si inicio con par da par"""

#COMPARACION

"""n=5
for i in range(n):
    print("si")
"""

"""n={2,3,5}
for i in range():
    print(n)  """ # NO SIRVE

#CUARTO EJERCICIO FOR
#Escribir un programa que pida al usuario un número entero positivo
#muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
"""n = int(input("Introduce un número entero positivo: "))
for i in range(n, -1, -2):
    print(i, end=", ")"""

#QUINTO EJERCICIO FOR
#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años
# muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

amount = float(input("¿Cantidad a invertir? "))
interest = float(input("¿Interés porcentual anual? "))
years = int(input("¿Años?"))
for i in range(years):
    amount *= 1 + interest / 100 
    print("Capital tras " + str(i+1) + " años: " + str(round(amount, 2)))


#SEXTO EJERCICIO FOR
#Escribir un programa que pida al usuario un número entero
#muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(n):
   print("*"*(i+1))

#SEPTIMO EJERCICIO FOR
#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

for i in range(1, 11):
    for j in range(1, 11):                            #COMO ES POSIBLE?!
        print(i*j, end="\t")
    print("")