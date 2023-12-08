import math
import numpy as np
from collections import Counter
from functools import cmp_to_key

def find_solution(mapping, current, target_fun):
    count = 0
    while not target_fun(current):
        instruction = instructions[count%len(instructions)]
        if instruction == 'L':
            current = mapping[current][0]
        elif instruction == 'R':
            current = mapping[current][1]
        count += 1
    return count

with open('8/input.txt', 'r') as f:
    input = f.read().split('\n\n')
    instructions = input[0]
    mapping = {}
    for line in input[1].split('\n'):
        arr = line.split(' = ')
        arr[1] = arr[1].replace('(','').replace(')','').split(', ')
        mapping[arr[0]] = arr[1]
    
    # part1
    print(find_solution(mapping, 'AAA', lambda x: x == 'ZZZ'))


    #part2   
    start_nodes = [node for node in mapping.keys() if node[2] == 'A']
    map_cycles = []
    for current in start_nodes:
        map_cycles.append(find_solution(mapping, current, lambda x: x[2] == 'Z'))
    print(np.lcm.reduce(np.array(map_cycles, dtype=np.int64)))


    
    



    