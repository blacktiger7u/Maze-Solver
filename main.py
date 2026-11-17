# This is the main file to start your project
# You may add any additional modules and other files you wish

# ALGORITHM PROVIDED DOES NOT GUARANTEE THE SHORTERT ROUTE

# 1. first i will load up the file
# 2. then i will using 2 for loops go with each line for pathfinding
# 3. then i will exclude impossible routes and change them to . (replace it after)
# 4. find the one possible and replace it by *
# 5. prints out the solution and steps
# PROBLEM: Error handling
# PROBLEM: adjustment to rules
# PROBLEM: code aint clear

from interface import choose_file, print_maze
from maze_files import load_file
from maze import solve

choice = choose_file()
coords = load_file(choice)
steps = solve(coords)
print_maze(coords, steps)