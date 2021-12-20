from datetime import datetime
print(datetime.today().isocalendar().year)

print("hi, we are going to do a division, write the first number")
dividend = int(input())
print("nice, now write the second number")
divider = int(input())
if(divider == 0):
    print("error")
else:
    result = dividend / divider
    print(result)