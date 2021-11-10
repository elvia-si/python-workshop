#temperature = 10

#if temperature > 30:
#    print('It\'s too hot')
#elif temperature > 40:
#    print('We\'re on fire')
#else:
#    print('it\'s ok')

apples = input('How many apples do you want?')

print(apples)

apples_weight = input('Do you want to weight them in kg or lbs?')

if apples_weight == 'kg':
    weight = int(apples) / 5
    print('Apples\'s weight is ' + str(weight) + ' kg')
elif apples_weight == 'lbs':
    weight = 2.205 * int(apples)/5
    print('Apples\'s weight is ' + str(weight) + ' lbs')
else:
    print('Invalid input')









