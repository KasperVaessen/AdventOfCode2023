with open('5/input.txt', 'r') as f:
    input = f.read().split('\n\n')
    seeds = input.pop(0).split()[1:]
    seeds = [int(seed) for seed in seeds]

    maps = [fun.split('\n') for fun in input]
    maps = [fun[1:] for fun in maps]
    maps = [[line.split(' ') for line in fun] for fun in maps]
    maps = [[[int(num) for num in line] for line in fun] for fun in maps]
    maps = [sorted(group, key=lambda x: x[1]) for group in maps]
    
    def convert(seed, map):
        for rule in map:
            dest_start = rule[0]
            source_start = rule[1]
            range_ = rule[2]
            if source_start <= seed <= source_start + range_:
                return dest_start + seed - source_start
        return seed
    
    locs = []
    for seed in seeds:
        for map in maps:
            seed = convert(seed, map)
        locs.append(seed)
    print(min(locs))
    
    def convert_recursive(seed, maps, level=0):
        if level == len(maps):
            return seed[0]
        map = maps[level]

        new_ranges = set()
        s1 = seed[0]
        s2 = seed[1]
        for rule in map:
            r1 = rule[1]
            r2 = rule[1]+rule[2]-1
            r3 = rule[0]

            if s1 < r1:
                if s2 < r1:
                    new_ranges.add((s1, s2))
                    s1 = s2+1
                    break
                new_ranges.add((s1, r1-1))
                s1 = r1
            if r1 <= s1 <= r2:
                if s2 > r2:
                    diff = r3-r1
                    new_ranges.add((s1+diff, r2+diff))
                    s1= r2+1
                elif s2 <= r2:
                    diff = r3-r1
                    new_ranges.add((s1+diff, s2+diff))
                    s1 = s2+1
                    break
        if s1 <= s2:
            new_ranges.add((s1, s2))
        
        
        min_sol = 1000000000000
        for s in new_ranges:
            sol = convert_recursive(s, maps, level+1)
            min_sol = min(sol, min_sol)
        return min_sol
    
    min_sol = []
    for s1, s2 in zip(seeds[::2], seeds[1::2]):
        min_sol.append(convert_recursive((s1,s1+s2-1), maps))
    print(min(min_sol))
    
