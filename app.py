import PySimpleGUI as sg
import  random
from util import calc_win, Player

options = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}

rev_options = {options[k]:k for k in options.keys()}


layout = [[sg.Text('A Sweet Rock, Paper, Scissors Gam')], 
          [sg.Text('Choose: ', size=(7, 1)), 
           sg.Combo([i for i in options.values()], default_value=list(options.values())[0], key = 'choice'),
           sg.Button('Play', key = 'play_btn')],
           [sg.Text('', key = 'result', auto_size_text=False)]]

window = sg.Window('RPS', layout=layout)


def main(window, p1,p2):
    while True:
        events, values = window.read()
        if events in (None, 'Exit'):
            break
        if events == 'play_btn':
            p1.choice = rev_options[values['choice']]
            p2.choice = random.randint(1, 3)

            winner = calc_win(p1, p2)
            if winner == None:
                p1.add_draw()
                print(f"DRAW on {options[p1.choice]}")
                window['result'].update(f'DRAW on {options[p1.choice]}')
            else:
                winner.add_win()
                print(winner.name, 'WON')
                ref = 'You' if winner.name == p1.name else winner.name
                window['result'].update(f'{ref} WON')

if __name__ == '__main__':
    p1 = Player(sg.popup_get_text('Enter Your Name: '))
    p2 = Player('Computer')

    main(window, p1, p2)

