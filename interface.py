import os


def choose_file():
    if not os.path.exists("mazes"):
        print("mazes folder does not exist!")
        exit()
    files = os.listdir("mazes")
    available=[]
    for filename in files:
        if filename.endswith(".txt"):
            available.append(filename)
    available.sort()
    for x in range(len(available)):
        print(f"{x+1}. {available[x]}")

    filechoice = input(f"choose a number between 1 and {len(available)}: ")
    if filechoice.isdigit() == False:
        print(f"invalid choice(choose a number between 1 and {len(available)} ")
        exit()
    filechoice = int(filechoice)
    if filechoice >= 1 and filechoice <= len(available):
        choice = available[(filechoice-1)]
    else:
        print(f"invalid choice(choose a number between 1 and {len(available)} ")
        exit()
    return choice


def print_maze(coords, steps):
    for line in coords:
        print("".join(line).replace("."," "))
    print(f"the maze took {steps} steps")