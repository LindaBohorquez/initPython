# esto es comentqario
#condicionales .
#if else
#bool true or false
edad1 = 45
limite = 18
edad2 = 25

if(edad1 > limite and edad2 > limite):
    print("pasa condicion")
else: 
    print("no pasa condicion")

#ejercicio
# pedir al usuario la edad
# y le debes decir si nacio antes del 2000

print("hi, what old are?")
age = input()
result = 2021 - int(age)  
if(result > 2000):
    print("born after year 2000, in year", result)
else:
    print("born before year 2000, in year", result)
