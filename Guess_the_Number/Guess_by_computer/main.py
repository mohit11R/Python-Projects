import random


def computer_guess(x):
    low = 1
    high = x
    feedback = ""

    while feedback != "c":
        if low != high:
            guess = random.randint(low , high)
        else:
            guess = low  # it could be high b/c low = high
        feedback = input(f"Is {guess} Too High (H), Too Low (L) , Correct (C)??  ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"Yay! Computer guessed Your Number {guess} Correctly.")


x = int(input("Enter the Range Value : "))
computer_guess(x)
