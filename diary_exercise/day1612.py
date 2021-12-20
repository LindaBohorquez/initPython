#variables
name: str
gender: str
letter: str
groupM = ["A","B","C","L","U"]
groupN = []

#logica
print("hi, what is your name")
name = input()
print("nice, now what is your gender, female (f) or male (m)")
gender = input()
letter = name[0] #ACCEDER A LA POSISION
print(letter)

if(groupM.index(letter) >= 0):
    print('grupo m')
else:
    print('grupo h')