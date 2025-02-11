x = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
y = [x for x in range(16, 0, -1)]
points = []
for n in range(3):    
    for yi in y:
        for index in range(3):
            points.append((x[n][index], yi))
