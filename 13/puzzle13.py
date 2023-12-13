import functools
import math

def change_smudge(field, allowed_mistakes):
    for i in range(len(field)-1):
        rows_top = [x for x in range(i, -1,-1)]
        rows_bottom = [x for x in range(i+1, len(field))]
        min_len = min(len(rows_top), len(rows_bottom))
        rows_top = rows_top[:min_len]
        rows_bottom = rows_bottom[:min_len]

        faults = 0
        for x,y in zip(rows_bottom, rows_top):
            for j in range(len(field[x])):
                if field[x][j] != field[y][j]:
                    faults += 1
        if faults == allowed_mistakes:
            return (i+1)*100
    
    for i in range(len(field[0])-1):
        columns_top = [x for x in range(i, -1,-1)]
        columns_bottom = [x for x in range(i+1, len(field[0]))]
        min_len = min(len(columns_top), len(columns_bottom))
        columns_top = columns_top[:min_len]
        columns_bottom = columns_bottom[:min_len]

        faults = 0
        for x,y in zip(columns_bottom, columns_top):
            for j, row in enumerate(field):
                if row[x] != row[y]:
                    faults += 1
        if faults == allowed_mistakes:
            return i+1

with open('13/input.txt', 'r') as f:
    input = [line.split('\n') for line in f.read().split('\n\n')]
    input = [[[x for x in line] for line in field]for field in input]
    
    total = 0
    total2 = 0
    for field in input:
        total += change_smudge(field,0)
        total2 += change_smudge(field,1)
    print(total, total2)
    
    