from itertools import chain
from copy import deepcopy


def calc_weight(board):
    total = 0
    for i, line in enumerate(board):
        total += line.count('O')*(len(board)-i)
    return total

def tilt_north(board):
    for i in range(len(board[0])):
        current_blocked = -1
        for j in range(len(board)):
            if board[j][i] == '.':
                continue
            elif board[j][i] == '#':
                current_blocked = j
            elif board[j][i] == 'O':
                board[j][i] = '.'
                current_blocked += 1
                board[current_blocked][i] = 'O'
    return board

def tilt_south(board):
    for i in range(len(board[0])):
        current_blocked = len(board)
        for j in range(len(board)-1,-1, -1):
            if board[j][i] == '.':
                continue
            elif board[j][i] == '#':
                current_blocked = j
            elif board[j][i] == 'O':
                board[j][i] = '.'
                current_blocked -= 1
                board[current_blocked][i] = 'O'
    return board

def tilt_east(board):
    for j in range(len(board)):
        current_blocked = len(board[0])
        for i in range(len(board[0])-1,-1, -1):
            if board[j][i] == '.':
                continue
            elif board[j][i] == '#':
                current_blocked = i
            elif board[j][i] == 'O':
                board[j][i] = '.'
                current_blocked -= 1
                board[j][current_blocked] = 'O'
    return board

def tilt_west(board):
    for j in range(len(board)):
        current_blocked = -1
        for i in range(len(board[0])):
            if board[j][i] == '.':
                continue
            elif board[j][i] == '#':
                current_blocked = i
            elif board[j][i] == 'O':
                board[j][i] = '.'
                current_blocked += 1
                board[j][current_blocked] = 'O'
    return board

def perform_cycle(board):
    return tilt_east(tilt_south(tilt_west(tilt_north(board))))


with open('14/input.txt', 'r') as f:
    input = [[x for x in line] for line in f.read().split('\n')]

    #Part 1
    print(calc_weight(tilt_north(deepcopy(input))))


    #Part 2
    total_cycles = 1000000000
    found = []
    onecycle = input
    hashable = tuple(chain.from_iterable(onecycle))

    while hashable not in found:
        found.append(hashable)
        onecycle = perform_cycle(onecycle)
        hashable = tuple(chain.from_iterable(onecycle))

    loop_length = len(found) - found.index(hashable)
    
    leftover = (total_cycles-found.index(hashable)) % loop_length


    for i in range(leftover):
        onecycle = perform_cycle(onecycle)

    print(calc_weight(onecycle))
    

    
    
    
    