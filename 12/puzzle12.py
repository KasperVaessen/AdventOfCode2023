from functools import cache

@cache
def find_solution2(string, checksum, num_hash=0):
    if len(checksum) == 0:
        if len(string) == 0 or not '#' in string:
            return 1
        else:
            return 0
    if len(string) == 0:
        return 0
    
    if string[0] == '.':
        if num_hash > 0:
            if checksum[0] == num_hash:
                return find_solution2(string[1:], checksum[1:], 0)
            else:
                return 0
        else:
            return find_solution2(string[1:], checksum, 0)
    if string[0] == '#':
        if checksum[0] > num_hash:
            return find_solution2(string[1:],checksum, num_hash+1)
        else:
            return 0
    if string[0] == '?':
        if num_hash == 0:
            return find_solution2(string[1:], checksum, 1) + find_solution2(string[1:], checksum, 0)
        else:
            if checksum[0] > num_hash:
                return find_solution2(string[1:],checksum, num_hash+1)
            elif checksum[0] == num_hash:
                return find_solution2(string[1:], checksum[1:], 0)
            else:
                return 0

with open('12/input.txt', 'r') as f:
    input = f.read().split('\n')
    input = [line.split(' ') for line in input]
    input = [[line[0],line[1].split(',')] for line in input]

    total = 0
    total2 = 0
    for line in input:
        string = line[0] + '.'
        checksum = tuple([int(num) for num in line[1]])
        string2 = line[0] + '?' + line[0] + '?' + line[0] + '?' + line[0] + '?' + line[0] + '.' 
        checksum2 = tuple([int(num) for num in line[1]]*5)

        ans = find_solution2(string, checksum)
        ans2 = find_solution2(string2, checksum2)
        total += ans
        total2 += ans2
    print(total, total2)


