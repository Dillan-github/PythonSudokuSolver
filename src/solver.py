import sys
from pprint import pprint
# read in command line arguments
#filename = sys.argv[1]
filename = "tests/test2.txt"
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

def isUnique(r,row):
    # given a list of lists, find the unique value
    pos_count = 0
    for row_value in row:
        for pos_value in row_value:
            if pos_value == r:
                pos_count += 1
                if pos_count > 1:
                    return False
    return True

def stuckFix():
    for possible_counter in range(2,N):
        for pi in range(N):
            for pj in range(N):
                if len(possible[pi][pj]) == possible_counter:
                    # just choose one
                    possible[pi][pj] = [possible[pi][pj][0]]
                    return

stuck_counter = 0
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
            
            temp_row = possible[i]
            for temp_value in temp:
                if isUnique(temp_value,temp_row):
                    temp = [temp_value]
            
            # check col
            col = [0]*N
            for c in range(N):
                col[c] = puzzle[c][j]
            
            for c in col:
                if c in temp:
                    temp.remove(c)
            
            temp_col = [0]*N
            for tc in range(N):
                temp_col[tc] = possible[tc][j]
            
            for temp_value in temp:
                if isUnique(temp_value,temp_col):
                    temp = [temp_value]
            
            # check quadrant
            quad = getQuadrant(whichQuadrant(i,j),puzzle)
            for q in quad:
                if q in temp:
                    temp.remove(q)
            
            temp_quad = getQuadrant(whichQuadrant(i,j),possible)
            for temp_value in temp:
                if isUnique(temp_value,temp_quad):
                    temp = [temp_value]

            possible[i][j] = temp
            
            # check possible array for a puzzle update
            for x in range(N):
                for y in range(N):
                    if len(possible[x][y]) == 1 and possible[x][y][0] != -1:
                        puzzle[x][y] = possible[x][y][0]
                        possible[x][y][0] = -1
                        stuck_counter = 0
    if stuck_counter > N:
        print("Stuck")
        #stuckFix()
        stuck_counter = 0
        exit(0)

            
        #exit(0)
            
    stuck_counter += 1


# write answer to new file
answer_filename = "output/"+"".join(filename.split("/")[1].split(".")[:-1]) + "_answer.txt"
print("Solution saved in {}".format(answer_filename))
new_file = open(answer_filename, "w")
for r in puzzle:
    for c in r:
        new_file.write(str(c))
        if c != r[N-1]:
            new_file.write(", ")
    new_file.write("\n")
new_file.close()