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

4 4 <br>
1 2 3 4 <br>
5 6 7 8 <br>
9 10 11 0 <br>
13 14 15 12 <br>

---
# Output files:
