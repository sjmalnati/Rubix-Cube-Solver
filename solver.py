#rubix cube solver
#0 is front
#1 is R
#2 is Top
#3 is L
#4 is Bottom
#5 is Under
import numpy as np
import copy
import random

def rotate(cube, turnType):
    if turnType == 'F':
        #front
        main_face = 0

        faces = [2,3,4,1]
            
    if turnType == 'R':
        #right turn
        main_face = 1
    if turnType == 'L':
        #left turn
        main_face = 2
    if turnType == 'B':
        #back turn
        main_face = 3
    if turnType == 'U':
        #under turn
        main_face = 4
    if turnType == 'T':
        #top turn
        main_face = 5
    temp_side = np.zeros((3,3),dtype=int)
    for i,x in enumerate(cube[main_face]):
        for j,y in enumerate(cube[main_face][i]):
            print(f'i:{i} j:{j} {(2-j)%3} face:{main_face}')
            temp_side[i][j] = cube[main_face][(2-j)%3][i]
    cube[main_face] = temp_side
    temp_cube = copy.deepcopy(cube)
    #counter clockwise rotation?
    #cube[faces[0]][2][:] = temp_cube[faces[1]][:][2]
    #cube[faces[1]][:][0] = temp_cube[faces[2]][2][:]
    #cube[faces[2]][0][:] = temp_cube[faces[3]][:][0]
    #cube[faces[3]][:][2] = temp_cube[faces[0]][0][:]
    
    cube[faces[0],2,:] = temp_cube[faces[3],:,2]
    cube[faces[1],:,0] = temp_cube[faces[0],2,:]
    cube[faces[2],0,:] = temp_cube[faces[1],:,0]
    cube[faces[3],:,2] = temp_cube[faces[2],0,:]
    
    return(cube)

def shuffle(cube):
    l=['F','B','R','L','T','U']
    for x in range(10):
        i = random.randint(0,6)
        cube=rotate(cube,l[i])


class create_cube():
    def __init__(self):
        temp = np.zeros((6,3,3),dtype=int)
        for i in range(6):
            for j in range(3):
                for k in range(3):
                    temp[i][j][k] = i
        self.cube=temp

first=create_cube()
k = 0
for i in range(3):
    for j in range(3):
        first.cube[0][i][j] = k
        k+=1

print(first.cube)
first.cube = rotate(first.cube,'F')
print(first.cube)

