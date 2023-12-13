import functools
import math

with open('13/testinput.txt', 'r') as f:
    input = [line.split('\n') for line in f.read().split('\n\n')]
    
    total = 0
    for field in input:
        
        for i in range(len(field)-1):
            rows_top = [x for x in range(i, -1,-1)]
            rows_bottom = [x for x in range(i+1, len(field))]
            min_len = min(len(rows_top), len(rows_bottom))
            rows_top = rows_top[:min_len]
            rows_bottom = rows_bottom[:min_len]

            symetric = True
            for x,y in zip(rows_bottom, rows_top):
                if field[x] != field[y]:
                    symetric = False
            if symetric:
                total += (i+1)*100

        
        for i in range(len(field[0])-1):
            columns_top = [x for x in range(i, -1,-1)]
            columns_bottom = [x for x in range(i+1, len(field[0]))]
            min_len = min(len(columns_top), len(columns_bottom))
            columns_top = columns_top[:min_len]
            columns_bottom = columns_bottom[:min_len]

            symetric = True
            for x,y in zip(columns_bottom, columns_top):
                if any([row[x] != row[y] for row in field]):
                    symetric = False
            if symetric:
                total += (i+1)
    print(total)

    #Part 2
    total = 0
    for field in input:
        faults = 0

        for i in range(len(field)-1):
            rows_top = [x for x in range(i, -1,-1)]
            rows_bottom = [x for x in range(i+1, len(field))]
            min_len = min(len(rows_top), len(rows_bottom))
            rows_top = rows_top[:min_len]
            rows_bottom = rows_bottom[:min_len]

            symetric = True
            switch = ()
            for x,y in zip(rows_bottom, rows_top):
                for j in range(len(field[x])):
                    if field[x][j] != field[y][j]:
                        if faults == 0:
                            faults += 1
                            switch = (x,j)
                        else: 
                            symetric = False
                if faults == 1:
                    field[switch[0]][switch[1]] = '#' if field[switch[0]][switch[1]] =='.' else '.'
            if symetric:
                total += (i+1)*100

        
        for i in range(len(field[0])-1):
            columns_top = [x for x in range(i, -1,-1)]
            columns_bottom = [x for x in range(i+1, len(field[0]))]
            min_len = min(len(columns_top), len(columns_bottom))
            columns_top = columns_top[:min_len]
            columns_bottom = columns_bottom[:min_len]

            symetric = True
            for x,y in zip(columns_bottom, columns_top):
                if any([row[x] != row[y] for row in field]):
                    symetric = False
            if symetric:
                total += (i+1)
    print(total)
    
    