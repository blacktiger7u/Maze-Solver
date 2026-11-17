def solve(coords):
    steps = 0
    started = False
    path = []

    for i in range(len(coords)):
        for j in range(len(coords[i])):
            if coords[i][j] == "S":
                started = True
                start = (i, j)
                minstarti = i
                minstartj = j
            elif coords[i][j] == "E":
                end = (i, j)
    path.append(start)
    i = minstarti
    j = minstartj
    while started:
        if (i,j) == end:
            break
        if coords[i-1][j] == " " or coords[i-1][j] == "E":
            i-=1
        elif coords[i+1][j] == " " or coords[i+1][j] == "E":
            i+=1
        elif coords[i][j-1] == " " or coords[i][j-1] == "E":
            j-=1
        elif coords[i][j+1] == " " or coords[i][j+1] == "E":
            j+=1
        else:
            if coords[i][j] == "*":
                coords[i][j] = "."
            path.pop()
            steps -= 1
            if len(path) == 0:
                print("invalid route")
                break
            i = path[-1][0]
            j = path[-1][1]
            continue
        path.append((i,j))
        steps += 1
        if coords[i][j] == " ":
            coords[i][j] = "*"
    return steps