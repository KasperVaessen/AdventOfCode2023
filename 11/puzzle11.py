def calculate_distance(galaxies, expansion_factor):
    distances = []
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            rows_distance = abs(galaxies[i][0]-galaxies[j][0])
            columns_distance = abs(galaxies[i][1]-galaxies[j][1])
            
            for inserted in rows_added:
                if galaxies[i][0] <= inserted <= galaxies[j][0]:
                    rows_distance += (expansion_factor-1)
                if galaxies[j][0] <= inserted <= galaxies[i][0]:
                    rows_distance += (expansion_factor-1)
            for inserted in columns_added:
                if galaxies[i][1] <= inserted <= galaxies[j][1]:
                    columns_distance += (expansion_factor-1)
                if galaxies[j][1] <= inserted <= galaxies[i][1]:
                    columns_distance += (expansion_factor-1)

            distance = rows_distance+columns_distance
            distances.append(distance)
    return sum(distances)

with open('11/input.txt', 'r') as f:
    universe = f.read().split('\n')

    #find rows which will be expanded
    i = 0
    rows_added = []
    while i < len(universe):
        if all([item == '.' for item in universe[i]]):
            rows_added.append(i)
        i+=1
    
    #find columns which will be expanded
    i=0
    columns_added = []
    while i < len(universe[0]):
        column = [row[i] for row in universe]
        if all([item == '.' for item in column]):
            columns_added.append(i)
        i+=1

    #find locations of galaxies
    galaxies = []
    for i in range(len(universe)):
        for j in range(len(universe[i])):
            if universe[i][j] == '#':
                galaxies.append((i,j))

    #calculate distances
    for i in (2,1000000):
        print(calculate_distance(galaxies,i))
    
    
    


    
    
    


    
    



    