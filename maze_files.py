def load_file(choice):
    with open(f"mazes/{choice}") as file:
        coords = []
        for line in file:
            x = line.rstrip("\n")
            coords.append(list(x))
    return coords