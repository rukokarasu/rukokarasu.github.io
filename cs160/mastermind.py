import random

RED = 'R'
YELLOW = 'Y'
GREEN = 'G'
BLUE = 'B'
COLORS = [RED, YELLOW, GREEN, BLUE]

def main():
    print('Possible colors: ' + ' '.join(COLORS))
    replay = True
    while replay:
        win = False
        code = makeCode(COLORS, 4)
        for turnCount in range(0, 12):
            guess = list(input('? '))
            print(feedback(list(code), list(guess)))
            if guess == code:
                win = True
                break
        if win:
            print('You win')
        else:
            print('You lose')
        print('Would you like to play again? (y/N)')
        replay = input('> ') in ['y', 'yes']


def makeCode(colors, length):
    return random.choices(colors, k=length)

def feedback(code, guess):
    out = ''
    length = len(code)

    for i in range(0, length):
        if guess[i] == code[i]:
            out += 'C'
            code[i] = '_'

    for i in range(0, length):
        if guess[i] in code:
            out += 'W'
            code[code.index(guess[i])] = '_'

    return out

if __name__ == '__main__':
    main()
