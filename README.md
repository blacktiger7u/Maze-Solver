# Maze Solver

Python Program that reads the maze from a text file, Searches the route by using DFS and draws the correct rout and prints the steps and the graph

## File format for mazes

`#` wall
` ` open cell
`S` start, `E` exit
`*` path

Input:
```text
 #S    #     #
 # ### # ### #
 #   #   #   #
 ### ##### # #
 #         #E#
 #############
```
## Output
```text
 #############
 #S    #     #
 #*### # ### #
 #***#   #***#
 ###*#####*#*#
 #  *******#E#
 #############
```
the maze took 18 steps

