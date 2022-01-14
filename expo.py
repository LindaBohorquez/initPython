# PRIMER EJERCICIO
# Comprobar si el usuario introduce un numero, si no es numero indicar que esta mal.
# Si es numero, decir si es par o impar

# Prueba
"""texto = "hola"
numero = "123"
maria = 1
print(texto.isnumeric())
print(numero.isnumeric())

# Resuleta la prueba seguiremos con el ejercicio
# SOLUCION
num = input("escribe un numero entero positivo ")
if(not(num.isnumeric())):
    print("Datos incorrectos, no es un numero")
else:
    if(num == "0"):
        print('es cero')
    else:
        num = int(num)
        if(num%2 == 0):
            print("es par")
        else:
            print("es impar")"""


# SEGUNDO EJERCICIO 
# CONCATENAR + ''
"""def saludarMaria(nombre):
    return ' holii' +nombre+ ' que tal' 
    
def saludarDos(nombre, funcion):
    return nombre + funcion('Maria')

resultado = saludarDos('Valen', saludarMaria)
print(resultado)"""


# TERCER EJERCICIO 
"""def maximo(num1, num2):
    if((type(num1)==int or type(num1) ==float) and (type(num2) == int or type(num2) == float)):
        if(num1 == num2):
            print("equal")
            return num1
        elif(num1 > num2): 
            return num1
        else:
             return num2
    else: 
        print("error")
        return False

num = maximo(3, 10)
if(type(num) != bool):
    print("el maximo es: " + str(num))

num = maximo(3, "azul")
if(type(num) != bool):
    print("el maximo es: " + str(num))  #entonces pa q sirve el bool? -_-"""



# CUARTO EJERCICIO 
# mini calculadora. se le pide al usuario una operacion y dos numeros.
# operaciones: suma, resta, multiplicacion, division, potencias.
# si se introduce una operacion diferete o algo diferente mostrar error

"""def calculator():
    operation = input("¿Que operación desea realizar?. las operaciones son:\n(+)\n(-)\n(*)\n(/)\n")
    
    num1 = (input("numero 1: "))
    num1 = validateNumber(num1) 
    num2 = (input("numero 2: "))
    num2 = validateNumber(num2)
    
    toDoOperation(operation, num1, num2)

def suma(num1, num2):
    return(num1 + num2)

def resta(num1, num2):
    return(num1 - num2)

def multiplicacion(num1, num2):
    return(num1 * num2)

def division(num1, num2):
    return(num1 / num2)

def validateNumber(num):
    if(not(num.isnumeric())):
        print("error")
        return -1
    else:
        return float(num) 

def toDoOperation(operation, num1, num2):
    if(operation == ("(+)")):
        print(suma(num1, num2))
    elif(operation == "(-)"):
        print(resta(num1, num2))
    elif(operation == "(*)"):
         print(multiplicacion(num1, num2))
    elif(operation == "(/)"):
         print(division(num1, num2))
    else:
        print("error.las operaciones son:\n-suma\n-resta\n-multiplicacion\n-division\n-potencia\n")

calculator()"""

numeros = [1, 2, 3, 4, 5,2, 90] 
"""print(numeros[2])
print(numeros)

# recorro la lista numeros con el for
for x in numeros:
    print(x*1000)"""

palabra = "maria hola"
count = ''

for x in numeros:
        count = count + '*'
        print(count)

"""for letra in palabra:
    if(letra == "a"):
        count = count + 1"""
        
#print(count)

    
sum = 0 
list = [1, 4, 2, 3, 7]
for ele in range(0, len(list)):
    sum = sum + list[ele]
print("sum", sum)