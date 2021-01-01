import random

def user_guess(x):
    random_number = random.randint(1,x)
    guess = 0 

    while guess != random_number :
        guess = int(input(f"Guess the number between 1 and {x}: "))
        if guess > random_number :
            print(f"No , You guess too high!")
        elif guess < random_number :
            print(f"No, You guess too low!")

    print(f"Yeah! You guess right")


x = int(input("Enter the value: "))
user_guess(x)