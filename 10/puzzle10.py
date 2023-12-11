import functools

def dir_s(board, current):
    if current[0]-1 >= 0 and board[current[0]-1][current[1]] in ['|', '7', 'F']:
        return (current[0]-1,current[1])
    if current[1]-1 >= 0 and board[current[0]][current[1]-1] in ['F', '-', 'L',]:
        return (current[0],current[1]-1)
    if current[0]+1 < len(board) and board[current[0]+1][current[1]] in ['|', 'L', 'J',]:
        return (current[0]+1,current[1])
    if current[1]+1 < len(board[0]) and board[current[0]][current[1]+1] in ['J', '-', '7']:
        return (current[0],current[1]+1)

def flood_outside(board, edge, current=(0,0)):
    unvisited = [current]
    flooded = set([current])

    while unvisited:
        possible = []
        y,x = unvisited.pop()
        if y - 1 >= -1 and (y-1,x) not in edge and (y-1,x) not in flooded:
            flooded.add((y-1,x))
            possible.append((y-1,x))
        if y + 1 <= len(board) and (y+1,x) not in edge and (y+1,x) not in flooded:
            possible.append((y+1,x))
            flooded.add((y+1,x))
        if x - 1 >= -1 and (y,x-1) not in edge and (y,x-1) not in flooded:
            possible.append((y,x-1))
            flooded.add((y,x-1))
        if x + 1 <= len(board[0]) and (y,x+1) not in edge and (y,x+1) not in flooded:
            possible.append((y,x+1))
            flooded.add((y,x+1))

        for node in possible:
            unvisited.append(node)
    return flooded
    


with open('10/testinput.txt', 'r') as f:
    input = f.read().split('\n')
    start_tile = ()
    for i, line in enumerate(input):
        if 'S' in line:
            start_tile = (i, line.index('S'))
    
    prev = start_tile
    current = dir_s(input, start_tile)
    count = [current]
    while current != start_tile:
        val_current = input[current[0]][current[1]]
        new_prev = current

        if val_current == '-':
            if current[1] > prev[1]:
                current = (current[0],current[1]+1)
            else:
                current = (current[0],current[1]-1)
        elif val_current == '7':
            if current[1] > prev[1]:
                current = (current[0]+1,current[1])
            else:
                current = (current[0],current[1]-1)
        elif val_current == '|':
            if current[0] > prev[0]:
                current = (current[0]+1,current[1])
            else:
                current = (current[0]-1, current[1])
        elif val_current == 'J':
            if current[0] > prev[0]:
                current = (current[0], current[1]-1)
            else:
                current = (current[0]-1, current[1])
        elif val_current == 'L':
            if current[0] > prev[0]:
                current = (current[0], current[1]+1)
            else:
                current = (current[0]-1, current[1])
        elif val_current == 'F':
            if current[0] < prev[0]:
                current = (current[0], current[1]+1)
            else:
                current = (current[0]+1, current[1])
        else:
            print('oeps')
        count.append(current)
        prev = new_prev

    # flooded = flood_outside(input, count)
    # flooded = [tile for tile in flooded if  0 <= tile[0] < len(input) and 0 <= tile[1] < len(input[0])]

    # enclosed = len(input)*len(input[0])-len(flooded)-len(count)
    # print(enclosed)

    flood = []
    for i in range(len(input)):
        in_loop = False
        for j in range(len(input[i])):
            if (i,j) in count and input[i][j] != '-':
                in_loop = not in_loop
            # elif (i, j-1) in count and (i,j) not in count:
            #     in_loop = not in_loop
            if in_loop and (i,j) not in count:
                flood.append((i,j))
    print(flood)
    print(len(flood))

    for i in range(len(input)):
        for j in range(len(input[i])):
            if (i,j) in count:
                print(input[i][j], end='')
            elif (i,j) in flood:
                print('0', end='')
            else:
                print('.', end='')
        print('\n')
    


    
    
    


    
    



    