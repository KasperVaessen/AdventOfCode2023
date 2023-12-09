import functools

with open('9/input.txt', 'r') as f:
    input = [line.split() for line in f.read().split('\n')]
    input = [[int(num) for num in line] for line in input]
    
    predictions, predictions_start = [], []
    for line in input:
        last_values, first_values = [], []
        while not all(v==0 for v in line):
            last_values.append(line[-1])
            first_values.insert(0,line[0])
            line = [line[i+1]-line[i] for i in range(len(line)-1)]
        predictions.append(sum(last_values))
        predictions_start.append(functools.reduce(lambda a,b: b-a, first_values, 0))
    print(f"Part 1: {sum(predictions)}")
    print(f"Part 2: {sum(predictions_start)}")
    


    
    



    