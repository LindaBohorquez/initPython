userX = input("ingrese nombre de usuario X: ")
userO = input("ingrese nombre de usuario O: ")
winner = ""         # row
list1 = ["-", "-", "-"] # 1
list2 = ["-", "-", "-"] # 2
list3 = ["-", "-", "-"] # 3

def winVertical(value):
    if list1[0] == value and list2[0] == value and list3[0] == value:
        return True
    if list1[1] == value and list2[1] == value and list3[1] == value:
        return True
    if list1[2] == value and list2[2] == value and list3[2] == value:
        return True
    return False

def winHorizontal(value):
    if list1[0] == value and list1[1] == value and list1[2] == value:
        return True
    if list2[0] == value and list2[1] == value and list2[2] == value:
        return True
    if list3[0] == value and list3[1] == value and list3[2] == value:
        return True
    return False   

def winDiagonal(value):
    if list1[0] == value and list2[1] == value and list3[2] == value:
        return True
    if list1[2] == value and list2[1] == value and list3[0] == value:
        return True
    return False

def result():
    print('list1')
    for x in list1:
        print(x)

    print('list2')
    for x in list2:
        print(x)

    print('list3')
    for x in list3:
        print(x)

def turnUser(user, value):
    row = int(input("usuario "+user+" ingrese fila:"))
    if (row <= 3) and (row >= 1):
        column = int(input("usuario "+user+" ingrese columna:"))
        if (column <= 3) and (column >= 1):
            print('validar si se puede poner en la posición ')
            if row == 1:
                if(list1[column-1] == "-"):
                  list1[column-1] = value  
                  if winVertical(value) or winHorizontal(value) or winDiagonal(value):
                        return user    
            if row == 2:
                if(list2[column-1]  == "-"):
                    list2[column-1] = value
                    if winVertical(value) or winHorizontal(value) or winDiagonal(value):
                        return user
            if row == 3:
                if(list3[column-1]  == "-"):
                    list3[column-1] = value
                    if winVertical(value) or winHorizontal(value) or winDiagonal(value):
                       return user
        else:
            print(' no ingresó correctamente el valor.')
    else:
        print(' no ingresó correctamente el valor.')

    result()
    return ""

while winner ==  "":
    print("empieza el juego: ")
    winner = turnUser(userX, 'X')
    winner = turnUser(userO, 'O')
    print('winner ',winner)
    


