# ИИ угадывает число
import random

def computer_guess(x):
    lives = 0 
    low = 1
    hight = x
    feedback = ''
    while feedback != 'да':
        guess = random.randint(low, hight)
        feedback = input(f' Твое число {guess}? если больше то напишите (б), если меньше то (м), если верно то напишите (да)?').lower()
        lives += 1
        if feedback == 'м':
            hight = guess - 1
        elif feedback == 'б':
            low = guess + 1

    print(f'Ура! Я угадал твой номер {guess} человек, c {lives} попытки!')

computer_guess(100)
