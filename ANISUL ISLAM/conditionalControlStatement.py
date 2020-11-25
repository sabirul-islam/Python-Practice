# pass/fail
mark = 100

if mark >= 33:
    print('pass')

else:
    print('fail')

# largest number
num1 = 20
num2 = 30

if num1 > num2:
    print(num1)

else:
    print(num2)

print(num1 if num1 > num2 else num2) # ternary operator

#even / odd number
number = 6

if number % 2 == 0:
    print('Even Number')

else:
    print('Odd Number')

#Letter Grade
mark = 69

if mark > 100 or mark < 0:
    print ('Invalid Number')

elif mark >= 80 and mark <= 100:
    print ('A+')
elif 70 <= mark < 80:
    print ('A')
elif mark >= 60 and mark < 70:
    print ('A-')
elif mark >= 45 and mark < 60:
    print ('B')
elif mark >= 33 and mark < 45:
    print ('C')
else:
    print ('F')

#Nested If Else
if 7 > 3:
    if 7 > 8:
        print ('shimul')
    else:
        print ('sabirul islam')

# Bigger number between three items
num1 = 10
num2 = 20
num3 = 30

if num1 > num2:
    if num1 > num3:
        print(num1)
    else:
       print(num3)

if num2 > num1: # you can use else instead this line
    if num2 > num3:
        print(num2)
    else:
        print(num3)