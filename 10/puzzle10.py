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
    

with open('10/input.txt', 'r') as f:
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
        count.append(current)
        prev = new_prev


    flood = []
    for i in range(len(input)):
        in_loop = False
        last_char = '.'
        for j in range(len(input[i])):
            cur_val = input[i][j]
            if cur_val == 'S': 
                cur_val = 'L'
            if (i,j) in count:
                if cur_val == '|':
                    in_loop = not in_loop
                if cur_val == '7' and last_char == 'L':
                    in_loop = not in_loop
                if cur_val == 'J' and last_char == 'F':
                    in_loop = not in_loop
            if (i,j) in count:
                if cur_val != '-':
                    last_char = cur_val
            else:
                last_char = '.'
            if (i,j) not in count and in_loop:
                flood.append((i,j))
    print(int(len(count)/2),len(flood))
    


    
    
    


    
    



    