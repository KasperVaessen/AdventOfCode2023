import math
import numpy as np


with open('6/input.txt', 'r') as f:
    input = f.read().split('\n')

    #Part 1
    times = input[0].split()[1:]
    distances = input[1].split()[1:]
    times = [int(x) for x in times]
    distances = [int(x) for x in distances]
    
    optimals = []
    for i in range(len(times)):
        d = distances[i]
        t = times[i]

        lower_time = math.floor((t - math.sqrt(t**2 - 4*d)) / 2)+1
        upper_time = math.ceil((t + math.sqrt(t**2 - 4*d)) / 2)-1

        optimals.append(upper_time-lower_time+1)

    print(np.product(optimals))

    #Part 2
    t = int(input[0].split(':')[1].replace(' ',''))
    d = int(input[1].split(':')[1].replace(' ',''))
    lower_time = math.floor((t - math.sqrt(t**2 - 4*d)) / 2)+1
    upper_time = math.ceil((t + math.sqrt(t**2 - 4*d)) / 2)-1
    print(upper_time-lower_time+1)
    
    
    
