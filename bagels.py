import random

def number_generator(length):
    numbers = [number for number in '0123456789']
    random.shuffle(numbers)
    game_number = ''.join(numbers[:length])
    return game_number

def number_tester(number, length):
    if number.isdigit() and len(number) == length:
        return True
    print('must be a number of length {}'.format(length))
    return False

def compare(game_number, user_number):
    string = ''
    done = []
    for i in range(len(game_number)):
        if game_number[i] == user_number[i]:
            string += 'Fermi '
            done.append(game_number[i])
    for i in range(len(game_number)):
        if game_number[i] in user_number and game_number[i] not in done:
            string += "Pico "
            done.append(game_number[i])
    if len(string) == 0:
        return 'Bagels'
    return string

def game_type():
    turn_options = '2345'
    while True:
        length = input('How many numbers do you want to guess? 2, 3, 4, or 5? A normal game is 3')
        if length in turn_options:
            length = int(length)
            break
    print('The number you have to guess is {} digits long, you will have {} turns to guess it.'.format(length, length ** 2 + 1))
    return length, length ** 2 + 1

def play_bagels():
    print('\n' """Welcome to Bagels!
You will pick a number of digits to guess very soon. 
If there is a correct number but in the wrong position, you will recieve a Pico. 
If there is a a correct number in the right place, you will recieve a Fermi.
If there are no correct numbers, you will recieve a Bagels!!!""" '\n')
    length, turns = game_type()
    game_number = number_generator(length)
    turn = 1
    # print(game_number)
    while turn <= turns:
        print('\nTurn {}:'.format(turn))
        while True:
            user_number = str(input())
            valid = number_tester(user_number, length)
            if valid:
                break
        result = compare(game_number, user_number)
        print(result)
        if result == 'Fermi ' * length:
            print('Congrats, you have won')
            break
        turn += 1
    print('Game Over')
    print('Computer number was {}'.format(game_number))
        
play_bagels()

    