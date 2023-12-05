import re

help_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

with open('1/input.txt', 'r') as f:
    text = f.read().split('\n')

    nums = []
    for line in text:
        dig = []
        for char in line:
            if char.isdigit():
                dig.append(char)
        nums.append(int(dig[0]+dig[-1]))
    print(sum(nums))

    nums=[]
    for line in text:
        dig = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
        for i in range(len(dig)):
            if dig[i] in help_dict.keys():
                dig[i] = help_dict[dig[i]]
        nums.append(int(dig[0]+dig[-1]))
    print(sum(nums))
    
    
