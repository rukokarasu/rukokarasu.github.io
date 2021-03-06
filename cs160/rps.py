from enum import Enum
import random
import re

ROCK = 0
PAPER = 1
SCISSORS = 2
    
DRAW = 0
WIN = 1
LOSE = 2

MOVES = [ROCK, PAPER, SCISSORS]

OUTCOMES = [DRAW, WIN, LOSE]

red = '\033[91m'
blue = '\033[94m'
resetColor = '\033[97m'

def main():
    print('Hello.')
    print('Options: rock (r), paper (p), scissors (s).')
    choice = ''
    model = []
    scores = {
        'you': 0,
        'com': 0
    }
    while (choice != 'q'):
        print(resetColor, end='')
        choice = input('> ')
        if choice == 'q':
            print('Quitting.')
        else:
            you = read(choice)
            if (you != None):
                com = predict(model)
                model += [com, you]
                print('Computer threw', pretty(com))
                outcome = compare(you, com)
                score(outcome, scores)
            else:
                print('I don\'t understand that.')
    print('Final score:')
    print('You won', scores['you'], 'times.')
    print('Computer won', scores['com'], 'times.')

def score(outcome, scores):
    if outcome == WIN:
        scores['you'] += 1
        print(blue + 'You win.')
    elif outcome == LOSE:
        scores['com'] += 1
        print(red + 'Computer wins.')
    else:
        print('It\'s a draw.')

def predict(model):
    return random.choice(MOVES)

# WHOA WATCH OUT YOU'RE ABOUT TO ENTER THE ~HACKER ZONE~
def compare(you, them):
    return (you - them) % 3

def read(s):
    s = s.lower()
    s = re.sub(r'\W+', '', s)
    if s == 'rock' or s == 'r':
        return ROCK
    elif s == 'paper' or s == 'p':
        return PAPER
    elif s == 'scissors' or s == 's':
        return SCISSORS
    else:
        return None

def pretty(throw):
    if throw == ROCK:
        return 'rock'
    elif throw == PAPER:
        return 'paper'
    elif throw == SCISSORS:
        return 'scissors'
    else:
        return None

if __name__ == '__main__':
    main()
