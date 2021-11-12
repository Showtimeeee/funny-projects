# Угадай число

import random  

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Угадай число от 1 до {x}: '))
        if guess < random_number:
            print('Неверно! слишком мало, попробуйте еще!')
        elif guess > random_number:
            print('Неверно! слишком много, попробуйте еще!')
    print(f'Верно! это число {random_number}')

guess(100) # до какого числа

