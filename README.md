# About project

15 puzzle solver with usage of BFS,DFS,A* algorithms.<br>
Works best with 4x4 puzzle board but can be used with nonsquare boards as well.<br>
As it stands for BFS and DFS user can choose desired searching order and depth limit, in case of  A* user needs to choose between Hamming's and Manhattan metrics for calculating distance.<br>



# Context
The 15 puzzle consists of 15 squares numbered from 1 to 15 that are placed in a 4×4 box leaving one position out of the 16 empty. The goal is to reposition the squares from a given arbitrary starting arrangement by sliding them one at a time into goal configuration - ascending order starting with 1 to 15.
<p align="center">
  <img src="https://github.com/madrian98/15_puzzle_BFS_DFS_A-star/blob/main/README_Image/goal_state.png" />
  <p align="center"> Puzzle goal state</p>
</p>

# Input file
This is a text file in which the number of lines depends on the size of the frame. The first line contains two integers, w and k, separated by a space, which respectively determine the vertical (number of rows) and horizontal (number of columns) size of the frame. Each of the remaining lines contains k integers separated by spaces, which describe the position of individual puzzle elements, where a value of 0 represents an empty space.

---
**Example input**

```bash
4 4 
1 2 3 4 
5 6 7 8 
9 10 11 0 
13 14 15 12 
```
---
# Output files

## Solution file
This is a text file typically consisting of 2 lines. The first line contains an integer n, indicating the length of the found solution (i.e., the length of the sequence of moves corresponding to the shifts of the empty tile that will transform the puzzle from the given initial state to the target state). The second line consists of a sequence of n letters, representing the individual moves of the empty tile within the found solution, according to the representation provided in the table above. If the program did not find a solution for the given initial state, the file will consist of only 1 line, containing the number -1.

---
**Example solution file**

```bash
1 
D 
```
---

## Statistics file
This is a text file consisting of 5 lines, each containing a respective number representing:<br>

* 1st line (integer): the length of the found solution - the same value as in the solution file (if the program did not find a solution, the value is -1).
* 2nd line (integer): the number of visited states.
* 3rd line (integer): the number of processed states.
* 4th line (integer): the maximum achieved recursion depth.
* 5th line (floating-point number with a precision of 3 decimal places): the duration of the computational process in milliseconds.

---
**Example statistics file**

```bash
1 
4 
1 
1 
0.997 
```

---
