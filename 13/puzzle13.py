import functools
import math

def find_solution(field, allowed_mistakes):
    # Rows
    for i in range(len(field)-1):
        rows_top = [x for x in range(i, -1,-1)]
        rows_bottom = [x for x in range(i+1, len(field))]

        faults = 0
        for x,y in zip(rows_bottom, rows_top):
            for j in range(len(field[x])):
                if field[x][j] != field[y][j]:
                    faults += 1
        if faults == allowed_mistakes:
            return (i+1)*100
    
    # Columns
    for i in range(len(field[0])-1):
        columns_top = [x for x in range(i, -1,-1)]
        columns_bottom = [x for x in range(i+1, len(field[0]))]
        
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
        total += find_solution(field,0)
        total2 += find_solution(field,1)
    print(total, total2)
    
    