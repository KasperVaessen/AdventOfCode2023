import re
from collections import defaultdict

def had_surrounding_char(grid, i, j):
    chars = ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    check = False
    gear_loc = []
    if i > 0 and grid[i-1][j] not in chars:
        if grid[i-1][j] == '*':
            gear_loc.append((i-1, j))
        check = True
    if i < len(grid) - 1 and grid[i+1][j] not in chars:
        if grid[i+1][j] == '*':
            gear_loc.append((i+1, j))
        check = True
    if j > 0 and grid[i][j-1] not in chars:
        if grid[i][j-1] == '*':
            gear_loc.append((i, j-1))
        check = True
    if j < len(grid[i]) - 1 and grid[i][j+1] not in chars:
        if grid[i][j+1] == '*':
            gear_loc.append((i, j+1))
        check = True
    if i > 0 and j > 0 and grid[i-1][j-1] not in chars:
        if grid[i-1][j-1] == '*':
            gear_loc.append((i-1, j-1))
        check = True
    if i > 0 and j < len(grid[i]) - 1 and grid[i-1][j+1] not in chars:
        if grid[i-1][j+1] == '*':
            gear_loc.append((i-1, j+1))
        check = True
    if i < len(grid) - 1 and j > 0 and grid[i+1][j-1] not in chars:
        if grid[i+1][j-1] == '*':
            gear_loc.append((i+1, j-1))
        check = True
    if i < len(grid) - 1 and j < len(grid[i]) - 1 and grid[i+1][j+1] not in chars:
        if grid[i+1][j+1] == '*':
            gear_loc.append((i+1, j+1))
        check = True
    return check, gear_loc

with open('3/input.txt', 'r') as f:
    grid = f.read().split('\n')

    dct = defaultdict(set)
    list_of_numbers = []
    for i, line in enumerate(grid):
        curr_number = '0'
        include_curr = False
        gears = set()
        for j, char in enumerate(line):
            if char.isdigit():
                curr_number += char
                check, gear_loc = had_surrounding_char(grid, i, j)
                for loc in gear_loc:
                    gears.add(loc)
                if check:
                    include_curr = True
            if not char.isdigit() or j == len(line) - 1:
                if include_curr:
                    list_of_numbers.append(int(curr_number))
                    for gear in gears:
                        dct[gear].add(int(curr_number))
                curr_number = '0'
                gears = set()
                include_curr = False
    print(sum(list_of_numbers))

    sum = 0
    for nums in dct.values():
        if len(nums) == 2:
            sum += nums.pop() * nums.pop()
    print(sum)
