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
"""
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
"""
#SEPTIMO EJERCICIO FOR
#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

"""for i in range(1, 11):
    for j in range(1, 11):                            #COMO ES POSIBLE?!
        print(i*j, end="\t")
    print("")"""

"""list = [1, 2, 3, 4, 8]
for x in list:
    print(x)"""

"""b = 30
def fub(a, b = b):
    return a + b 
print(fub(1))"""

#8



# 3,5
"""km = (input("escribe un numero para saber la cantidad de km recorridos "))
if(not(km.isnumeric())):
    print("Datos incorrectos, no es un numero")
else:
    if float(km) > 0:
        liters = (input("escribe la cantidad de litros gastados en total "))
        if(not(liters.isnumeric())):
            print("Datos incorrectos, no es un numero")
        if float(liters) > 0:
            num = float(km) / float(liters)
            num = str(num)
            print(num + " es la cantidad de litros o mililitros gastado por km")
        else:
            print("error2")
    else:
        print("error1")"""

#9

"""print("ingrse un numero para generar la tabla")
n = int(input())
for i in range(1,10):
    x = n * i
    if (not((x)%2 == 0)):
        print(n, " x ", i, " = ", x)"""

#10 DUDA EJERCICIO 8 

"""print("A",end="")
print("B",end="")
print("C",end="")"""

#BUCLES WHILE
"""letraEncontrada = False
letra = "e"
frase = "en este momento estoy buscando la letra a"
indice = 0
while(not(letraEncontrada)):
    if(frase[indice] == "e"):
        letraEncontrada = True
        print(f"ya hemos encontrado la letra {letra} en la posicion {indice} !")
    else:
        indice += 1 """

#1 WHILE
# Hacer un programa que pida al usuario números enteros positivos,
# y se detenga hasta que el usuario ingrese el 0 cero.
# al ingresar cero se debe mostrar la sumatoria de todos los números,
#  ingresados por el usuario anterior al cero
# como asi? .-.

"""count = 0
value = -1
while(value != 0):
    value = int(input('ingrese numero '))
    if( value == 0):
        print(count)
    else:
        if(value > 0):
            count = count + value"""

    
#2 while
# Leer números enteros positivos de teclado, 
# hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.
"""count = 0
value = -1

while(value != 0):
    value = int(input('ingrese numero '))
    if( value == 0):
        print(count)
    else:
        if(value > 0):
            if(value > count):
                count = value

print('value '+ str(value))
print('count '+ str(count))"""


# 3 while
#Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.

suma=0
n=int(input("Número positivo:"))
while n!=0: 
    digito=n%10
    print(digito)
    suma+=digito 
    n=n//10
    print(n)
print("Suma de los dígitos:", suma)
division = 559.6 // 10 
print(division)

#4 while
# Crear un programa que permita al usuario procesar los montos de las compras de un cliente,
# cortando el ingreso de datos cuando el usuario ingrese el monto 0
# si infresa un monto negativo, no se debe procesar y se debe pedir que proporcione un monto nuevo.
# Al finalizar, informar el total a pagar teniendo en cuenta que, si las ventas superan el total de 
# $1000, se le debe aplicar un 10% de descuento 
"""
total = 0
monto = -1
while monto != 0:
    monto = float(input("escribe el monto de las compras "))
    if monto < 0:
        print ("monto no valido ")
    else:
        total += monto 

if total>1000:
    total = total - (total*0.1)   #otra manera seria (total -= total*0.1) 
print("monto total a pagar: $", total)"""