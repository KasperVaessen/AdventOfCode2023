import re

with open('2/input.txt', 'r') as f:
    text = f.read().split('\n')
    input = [re.sub(r'Game \d+: ', '', line) for line in text]
    input = [game.split('; ') for game in input]
    input = [[round.split(', ') for round in game] for game in input]
    input = [[[tuple(item.split(' ')) for item in round] for round in game] for game in input]

    ind  = []
    for i, game in enumerate(input):
        add = True
        for round in game:
            curr_blue = 0
            curr_red = 0
            curr_green = 0
            for item in round:
                if item[1] == 'blue':
                    curr_blue += int(item[0])
                elif item[1] == 'red':
                    curr_red += int(item[0])
                elif item[1] == 'green':
                    curr_green += int(item[0])
            if curr_blue > 14 or curr_red > 12 or curr_green > 13:
                add = False
        if add:
            ind.append(i+1)
    print(sum(ind))
    
    powers = []
    for i, game in enumerate(input):
        min_blue = 0
        min_red = 0
        min_green = 0
        for round in game:
            for item in round:
                if item[1] == 'blue':
                    min_blue = max(min_blue, int(item[0]))
                elif item[1] == 'red':
                    min_red = max(min_red, int(item[0]))
                elif item[1] == 'green':
                    min_green = max(min_green, int(item[0]))
        powers.append(min_blue * min_red * min_green)
    print(sum(powers))
        

