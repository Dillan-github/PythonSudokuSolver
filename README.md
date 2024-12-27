# Python Sudoku Solver
Initial commit ReadMe

src/solver.py will take in the filename as the only command line argument:
1. the path to the text file containing the unsolved puzzle


The text file containing the unsolved puzzle should be in the following format:

5, 3, 0, 0, 7, 0, 0, 0, 0\
6, 0, 0, 1, 9, 5, 0, 0, 0\
0, 9, 8, 0, 0, 0, 0, 6, 0\
8, 0, 0, 0, 6, 0, 0, 0, 3\
4, 0, 0, 8, 0, 3, 0, 0, 1\
7, 0, 0, 0, 2, 0, 0, 0, 6\
0, 6, 0, 0, 0, 0, 2, 8, 0\
0, 0, 0, 4, 1, 9, 0, 0, 5\
0, 0, 0, 0, 8, 0, 0, 7, 9

- Spaces will be ignored.
- 0 replresents an empty square

Example of execution from root directory:

```python3 src/solver.py 1 test1.txt```

This solves simple puzzles.