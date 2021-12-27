import PySimpleGUI as sg


def calc_win(p1, p2):
    if p1.choice == 1 and p2.choice == 2:
        return p2
    elif p1.choice == 1 and p2.choice == 3:
        return p1
    elif p1.choice == 2 and p2.choice == 1:
        return p1
    elif p1.choice == 2 and p2.choice == 3:
        return p2
    elif p1.choice == 3 and p2.choice == 1:
        return p2
    elif p1.choice == 3 and p2.choice == 2:
        return p1
    else:
        return None


class Player:
    def __init__(self, name, choice=0):
        self.name = name
        self.choice = choice
        self.win = 0
        self.draw = 0

    def add_win(self):
        self.win += 1

    def add_draw(self):
        self.draw += 1

    def get_stats(self, total):
        percentage_win = round((self.win / total) * 100, 2)
        percentage_lost = round(
            ((total - (self.win + self.draw)) / total) * 100, 2)
        percentage_draw = round((self.draw/total) * 100, 2)
        return {'win': (percentage_win, self.win),
                'lost': (percentage_lost, total - (self.win + self.draw)),
                'draw': (percentage_draw, self.draw)}

    def __repr__(self) -> str:
        return f'<Name {self.name}>'

def get_valid_input(sg):
    c = sg.popup_get_text('Enter your choice. \n "1" for Rock \n "2" for Paper \n "3" for Scissors')
    while c not in ['1', '2', '3']:
        sg.popup_auto_close('Invalid Choice', no_titlebar=True,
                            background_color='red', text_color='white', font="Arial white 16")
        c = sg.popup_get_text('Enter your choice. \n "1" for Rock \n "2" for Paper \n "3" for Scissors')
    return int(c)
