def solve(coords):
    steps = 0
    started = False
    ended = False
    path = []
    allowed = ["S", "E", "#", " "]
    visited = set()
    for k in coords:
        if len(k) != len(coords[0]):
            print("maze must have the same length of rows")
            exit()

    for i in range(len(coords)):
        for j in range(len(coords[i])):
            if coords[i][j] not in allowed:
                print("forbidden signs at the loaded maze")
                exit()
            if coords[i][j] == "S" and started:
                print("maze has another S, only one is allowed")
                exit()
            if coords[i][j] == "E" and ended:
                print("maze has another E, only one is allowed")
                exit()
            if coords[i][j] == "S":
                started = True
                start = (i, j)
                minstarti = i
                minstartj = j
            elif coords[i][j] == "E":
                end = (i, j)
                ended = True
    if not ended or not started:
        print("maze must have the start and the end")
        exit()
    path.append(start)
    visited.add(start)
    i = minstarti
    j = minstartj
    while started:
        if (i,j) == end:
            break
        if (i-1,j) not in visited and (coords[i-1][j] == " " or coords[i-1][j] == "E"):
            i-=1
        elif (i+1,j) not in visited and (coords[i+1][j] == " " or coords[i+1][j] == "E"):
            i+=1
        elif (i,j-1) not in visited and (coords[i][j-1] == " " or coords[i][j-1] == "E"):
            j-=1
        elif (i,j+1) not in visited and (coords[i][j+1] == " " or coords[i][j+1] == "E"):
            j+=1
        else:
            if coords[i][j] == "*":
                coords[i][j] = "."
            path.pop()
            steps -= 1
            if len(path) == 0:
                print("maze is not solvable")
                exit()
            i = path[-1][0]
            j = path[-1][1]
            continue
        path.append((i,j))
        visited.add((i,j))
        steps += 1
        if coords[i][j] == " ":
            coords[i][j] = "*"
    return steps