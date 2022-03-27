import random

def guess(x):
    # random integer between 1 and x
    random_number = random.randint(1,x)
    users_guess = int(input(f'Enter yout guess number between 1 and {x}: '))
    while(users_guess != random_number):
        if(users_guess < random_number):
            users_guess = int(input('The secret number is higher. Try again: '))
        if(users_guess > random_number):
            users_guess = int(input('The secret number is lower. Try again: '))
    print(f'Congratulations, you won!. The secret number was {random_number}')

guess(10)