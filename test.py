import random
import sys
from util import *


options = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}

play_number = int(input('How many times do you want to play?\n >> '))
total_play = play_number


p1 = Player('human')
p2 = Player('computer')


while play_number > 0:
    p1.choice = get_valid_input()
    p2.choice = random.randint(1,3)

    winner = calc_win(p1, p2)
    if winner == None:
        p1.add_draw()
        print(f"DRAW on {options[p1.choice]}")
    else:
        winner.add_win()
        print(winner.name, 'WON')

    play_number -= 1



print(p1.get_stats(total_play))
sys.exit()
