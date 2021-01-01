import random

def play():

    user = input("What's your choice? 'r'for Rock, 's' for Scissor , 'p' for paper\n" )
    computer = random.choice(['r','s','p'])

    if user == computer:
        return "It's a tie!"
    
    # r > s, s > p, p > r
    if is_win(user,computer):
        return "You Won!"
    
    return "You Lost!"


def is_win(player,opponent):

    # return true if player wins
    # r > s, s > p, p > r

    if (player == "r" and opponent == 's') or (player == "s" and opponent == 'p') or (player == "p" and opponent == 'r'):
        return True



print(play())