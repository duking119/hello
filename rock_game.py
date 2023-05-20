import random


def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors \n")
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return 'It\'s a tie'
    
    if is_win(user,computer):
        return 'You win!'
    
    return 'You lost!'


def is_win(player, opponent):
    # return True if player is win
    # r>s s>p p>r
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') \
        or (player == 's' and opponent == 'p'):
        return True
    

print(play())