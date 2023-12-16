def follow_laser(layout, initial_loc = (0,0), initial_dir = (0,1)):
    visited = set()
    call_stack = [(initial_loc, initial_dir)]
    memo = set()
    
    while call_stack:
        current_pos, dir = call_stack.pop()

        if (current_pos, dir) in memo:
            continue
        memo.add((current_pos, dir))
        
        y, x = current_pos
        if not (0 <= y < len(layout) and 0 <= x < len(layout[0])):
            continue
        visited.add(current_pos)
        
        tile = layout[y][x]

        if (tile == '.') or (tile == '-' and dir in [(0,1),(0,-1)]) or (tile == '|' and dir in [(1,0),(-1,0)]):
            call_stack.append(((y+dir[0],x+dir[1]), dir))
        elif tile == '\\':
            dir = (dir[1],dir[0])
            call_stack.append(((y+dir[0],x+dir[1]), dir))
        elif tile == '/':
            dir = (-dir[1],-dir[0])
            call_stack.append(((y+dir[0],x+dir[1]), dir))
        elif tile in ['|','-']:
            dir1 = (dir[1],dir[0])
            dir2 = (-dir[1],-dir[0])
            call_stack.append(((y+dir1[0],x+dir1[1]), dir1))
            call_stack.append(((y+dir2[0],x+dir2[1]), dir2))
    return len(visited)

with open('16/input.txt', 'r') as f:
    input = f.read().split('\n')

    #Part 1
    print(follow_laser(input))

    #Part 2
    max_energised = 0
    for i in range(len(input)):
        start1, start2 = (i,0), (i,len(input)-1)
        dir1, dir2 = (0,1), (0,-1)
        max_energised = max(max_energised, follow_laser(input, start1, dir1))
        max_energised = max(max_energised, follow_laser(input, start2, dir2))
    for i in range(len(input[0])):
        start1, start2 = (0,i), (len(input[0])-1,i)
        dir1, dir2 = (1,0), (-1,0)
        max_energised = max(max_energised, follow_laser(input, start1, dir1))
        max_energised = max(max_energised, follow_laser(input, start2, dir2))

    print(max_energised)


    