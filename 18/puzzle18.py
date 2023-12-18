import numpy as np

def PolyArea(x,y):
    return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))

with open('18/input.txt', 'r') as f:
    instructions = f.read().split('\n')
    instructions = [line.split(' ') for line in instructions]

    dir_map = {
        'U': [-1,0],
        'R': [0,1],
        'D': [1,0],
        'L': [0,-1],
        '0': [0,1],
        '1': [1,0],
        '2': [0,-1],
        '3': [-1,0]
    }
    
    loop_corners1 = [[0,0]]
    int_coor1 = 0

    loop_corners2 = [[0,0]]
    int_coor2 = 0

    for ins in instructions:
        dir = dir_map[ins[0]]
        amount = int(ins[1])
        int_coor1 += amount
        loop_corners1.append([loop_corners1[-1][0]+dir[0]*(amount), loop_corners1[-1][1]+dir[1]*(amount)])
    
    for ins in instructions:
        dir = dir_map[ins[2][7]]
        amount = int(ins[2][2:7],16)
        int_coor2 += amount
        loop_corners2.append([loop_corners2[-1][0]+dir[0]*(amount), loop_corners2[-1][1]+dir[1]*(amount)])

    
    corners1 = np.array(loop_corners1)
    y1 = corners1[:,0]
    x1 = corners1[:,1]

    corners2 = np.array(loop_corners2, dtype=np.int64)
    y2 = corners2[:,0]
    x2 = corners2[:,1]

    # Pick's theorem rewritten
    print(PolyArea(x1,y1)-(int_coor1/2)+1+int_coor1)
    print(PolyArea(x2,y2)-(int_coor2/2)+1+int_coor2)
    
    




        




    