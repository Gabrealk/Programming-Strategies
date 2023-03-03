models = {
    'apple phone': 120.45,
    'android phone': 99.50,
    'apple tablet': 75.69,
    'android tablet': 65.73,
    'windows tablet': 51.49,
}


print('Welcome to Circle Phones Profit calculator\n')
print('You can calculate the profit of the company according to a specific day or by a week or divide the week into weekdays and weekend\n')

days = int(input('''Enter:
1-For a specific day
2-For the week
3-For the week buisness days
4-For weekend days
0-Exit\n'''))

day_value = 0



if (days > 4):
        print('invalid input, please enter a valid number')
elif days == 1:
        day_value+=1
elif(days == 2):
        day_value+=7
elif(days == 3):
        day_value+=5
elif(days == 4):
        day_value+=2
    #elif(days == 0):
        #break


sum = 0
while True:

    category = int(input('Enter product number 1-5, or enter 0 to stop:\n    '))

    if category > 5:
        print('Invalid input, please enter a valid number')

    elif category == 1:
        quantity = int(input('Enter quantity sold:\n    '))
        sum += (models['apple phone']*quantity)

    elif category == 2:
        quantity = int(input('Enter quantity sold:\n    '))
        sum += (models['android phone']*quantity)

    elif category == 3:
        quantity = int(input('Enter quantity sold:\n    '))
        sum += (models['apple tablet']*quantity)

    elif category == 4:
        quantity = int(input('Enter quantity sold:\n    '))
        sum += (models['android tablet']*quantity)

    elif category == 5:
        quantity = int(input('Enter quantity sold:\n    '))
        sum += (models['windows tablet']*quantity)

    if category == 0:
        sum = sum
        print('your total profit today is:',(sum * days))
        break