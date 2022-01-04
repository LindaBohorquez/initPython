# PRIMER EJERCICIO
# Comprobar si el usuario introduce un numero, si no es numero indicar que esta mal,
# Si es numero, decir si es par o impar

# Prueba
texto = "hola"
numero = "123"
print(texto.isnumeric())
print(numero.isnumeric())

# Resuleta la prueba seguiremos con el ejercicio
# SOLUCION
num = input("escribe un numero ")
if(not(num.isnumeric())):
    print("Datos incorrectos, no es un numero")
else:
    num = int(num)
    if(num%2 == 0):
        print("es par")
    else:
        print("es impar")


# SEGUNDO EJERCICIO 
# 