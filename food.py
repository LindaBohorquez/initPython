# food depending age
# ask to the user what age have
# depending the age we have to assign what kind of food they can eat

print("hi. how old are you?")
age = int (input())
if(age < 10):
    print("you have to eat chiken")
elif(age >= 10 and age < 15  ):
    print("you have to eat meat")
else:
    print("you have to eat tuna")