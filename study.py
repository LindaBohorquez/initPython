#   BOOLEANOS
#print("write your age")
#x = int(input())
#
#if(x >= 18):
#    print("adult")
#else:
#    print("younger")

#age = input("write your age")
#age = int(age)

#if(type(age) == int):
#    if(age > 120 or age < 0):
#        print("False")
#    elif(age >= 18 and age < 40):
#        print("you can in")
#    elif(age > 15 and age< 18):
#        print("too young")
#    else:
#        print("no condition accepted")
#else: 
#    print("it is not a whole number")

#Funciones 

def saludo(nombre):
    print("hola "+ nombre +" que tal?")
saludo("luz")

#Funciones con argumentos

def suma(a, b):
    return  a + b        #puede usar se una variable mas o no, es eleccion

valor = suma(22, 152)
print(valor)

#Funciones que retornan varios valores

def sumaYResta(a, b):
    suma = a + b
    resta = a - b
    return suma, resta              #Tambein se puede 
                                    # return a + b, a - b

resultado1, resultado2 = sumaYResta(10, 5)
print("Los Resultados son:\nSuma:" + str(resultado1) + "\nResta: "+ str(resultado2))
