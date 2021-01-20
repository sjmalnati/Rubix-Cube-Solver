#rubix cube solver
#0 is front
#1 is R
#2 is Top
#3 is L
#4 is Bottom
#5 is Under

def rotate(cube, turnType):
    if turnType == 'F':
        #front
        temp_side = [][]
        for i,x in enumerate(cube[0]):
            for j,y in enumerate(cube[0][i]):
                temp_side[i][j] = cube[(2-j)%3][i]
        temp_side = cube[0]
    if turnType == 'R':
        #right turn
    if turnType == 'L':
        #left turn
    if turnType == 'B':
        #back turn
    if turnType == 'U':
        #under turn
    if turnType == 'T':
        #top turn
    return(cube)
