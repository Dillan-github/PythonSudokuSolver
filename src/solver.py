import sys
from pprint import pprint
# read in command line arguments
#method = sys.argv[1]
#filename = sys.argv[2]
filename = "tests/test1.txt"
N = 9
# print("method: {}, filename: {}".format(method, filename))

# read file into array
puzzle = [0] * N
file = open(filename, "r")
i = 0
for line in file:
    lst = [0] * N
    lst_counter = 0
    for l in line.strip().split(","):
        lst[lst_counter] = int(l.strip())
        lst_counter += 1
    puzzle[i] = lst
    i+=1

file.close()

# print(puzzle)

def getQuadrant(x,a):
    switcher = {
        0: a[0][:3] + a[1][:3] + a[2][:3],
        1: a[0][3:6] + a[1][3:6] + a[2][3:6],
        2: a[0][6:10] + a[1][6:10] + a[2][6:10],
        3: a[3][:3] + a[4][:3] + a[5][:3],
        4: a[3][3:6] + a[4][3:6] + a[5][3:6],
        5: a[3][6:10] + a[4][6:10] + a[5][6:10],
        6: a[6][:3] + a[7][:3] + a[8][:3],
        7: a[6][3:6] + a[7][3:6] + a[8][3:6],
        8: a[6][6:10] + a[7][6:10] + a[8][6:10]
    }
    return switcher.get(x,"ERROR: no switch sase for x = {}".format(x))

def whichQuadrant(i,j):
    return 3 * (i // 3) + (j // 3)

def isSolved(a):
    solved = False
    for row in range(N):
        for col in range(N):
            if a[row][col] == 0:
                return(False)
    return(True)

# Array of possible values:
possible = [0]*N
for i in range(N):
    possible[i] = [0]*N
    for j in range(N):
        if puzzle[i][j] == 0:
            possible[i][j] = [1,2,3,4,5,6,7,8,9]
        else:
            possible[i][j] = [-1]


solved = False

# print(whichQuadrant(5,1))
count = 0
while not isSolved(puzzle):
    # loop through the puzzle
    for i in range(N):
        for j in range(N):
            # get the possible options for that square
            temp = possible[i][j]
            
            # check row
            row = puzzle[i]
            
            for r in row:
                if r in temp:
                    temp.remove(r)
            
            # check col
            col = [0]*N
            for c in range(N):
                col[c] = puzzle[c][j]
            
            for c in col:
                if c in temp:
                    temp.remove(c)
            
            # check quadrant
            quad = getQuadrant(whichQuadrant(i,j),puzzle)
            for q in quad:
                if q in temp:
                    temp.remove(q)
            
            possible[i][j] = temp
                   
            for x in range(N):
                for y in range(N):
                    if len(possible[x][y]) == 1 and possible[x][y][0] != -1:
                        puzzle[x][y] = possible[x][y][0]
                        possible[x][y][0] = -1

print("Puzzle:")
pprint(puzzle)