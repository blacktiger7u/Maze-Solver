import os


def choose_file():
    files = os.listdir("mazes")
    available=[]
    for filename in files:
        if filename.endswith(".txt"):
            available.append(filename)
    available.sort()
    for x in range(len(available)):
        print(f"{x+1}. {available[x]}")

    filechoice = int(input(f"choose a number between 1 and {len(available)}: "))
    if filechoice >= 1 and filechoice <= len(available):
        choice = available[int(filechoice-1)]
    else:
        print("invalid choice!")
    return choice


def print_maze(coords, steps):
    for line in coords:
        print("".join(line).replace("."," "))
    print(f"the maze took {steps} steps")