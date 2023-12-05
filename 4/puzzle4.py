import re

with open('4/input.txt', 'r') as f:
    input = f.read().split('\n')
    input = [re.sub(r'Card \d+: ', '', line) for line in input]
    input = [re.sub(r'Card  \d+: ', '', line) for line in input]
    input = [re.sub(r'Card   \d+: ', '', line) for line in input]
    input = [line.split('|') for line in input]
    input = [[numbers.split() for numbers in line] for line in input]
    input = [[set([int(number) for number in numbers]) for numbers in line] for line in input]

    lis = []
    for line in input:
        amount = len(line[0].intersection(line[1]))
        if amount > 0:
            lis.append(2**(amount-1))
    print(sum(lis))

    winners = []
    for i, line in enumerate(input):
        amount = len(line[0].intersection(line[1]))
        if amount > 0:
            winners.append(1)
        else:
            winners.append(0)


    amounts = [1 for _ in range(len(input))]
    
    
    for i, amount in enumerate(amounts):
        new_amount = len(input[i][0].intersection(input[i][1]))
        if new_amount > 0:
            amounts[i+1:i+new_amount+1] = [amount+am for am in amounts[i+1:i+new_amount+1]]
    print(sum(amounts))
