from itertools import chain
from copy import deepcopy
import re

def calculate_hash(str):
    current_value = 0
    for char in str:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value

with open('15/input.txt', 'r') as f:
    input = f.read().split(',')

    #Part 1
    total = 0
    for str in input:
        total += calculate_hash(str)
        
    print(total)

    #Part 2
    map = [[] for _ in range(256)]

    for str in input:
        key = re.search(r'[a-z]+', str).group()
        operation = re.search(r'=|-', str).group()
        num = re.search(r'\d+', str).group() if operation == '=' else None

        index = calculate_hash(key)
        
        box = map[index]
        found = False
        for i, lens in enumerate(box):
            if lens[0] == key:
                if operation == '-':
                    box.pop(i)
                    found = True
                    break
                if operation == '=':
                    box[i] = (key, num)
                    found = True
                    break
        if not found:
            if operation == '=':
                box.append((key, num))
    
    total = 0
    for i, box in enumerate(map):
        for j, lens in enumerate(box):
            num = (1+i)*(j+1)*int(lens[1])
            total += num
    print(total)
            


    

    
    
    
    