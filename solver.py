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

class create_cube():
    def __init__(self):
        temp = np.zeros((6,3,3),dtype=int)
        for i in range(6):
            for j in range(3):
                for k in range(3):
                    temp[i][j][k] = i
        self.cube=temp
    
    def rotate(self,turnType):
        temp_cube = copy.deepcopy(self.cube)
        if turnType == 'F':
            #front
            main_face = 0
            self.cube[2,2,:] = temp_cube[1,:,2]
            self.cube[3,:,0] = temp_cube[2,2,:]
            self.cube[4,0,:] = temp_cube[3,:,0]
            self.cube[1,:,2] = temp_cube[4,0,:]
        if turnType == 'R':
            #right turn
            main_face = 1
            self.cube[2,:,2] = temp_cube[0,:,2]
            self.cube[5,:,2] = temp_cube[2,:,2]
            self.cube[4,:,2] = temp_cube[5,:,2]
            self.cube[0,:,2] = temp_cube[4,:,2]
        if turnType == 'L':
            #left turn
            main_face = 3
            self.cube[2,:,0] = temp_cube[5,:,0]
            self.cube[0,:,0] = temp_cube[2,:,0]
            self.cube[4,:,0] = temp_cube[0,:,0]
            self.cube[5,:,0] = temp_cube[4,:,0]
        if turnType == 'B':
            #back turn
            main_face = 5
            self.cube[4,2,:] = temp_cube[1,:,0]
            self.cube[3,2,:] = temp_cube[4,2,:]
            self.cube[2,0,:] = temp_cube[3,2,:]
            self.cube[1,:,0] = temp_cube[2,0,:]
        if turnType == 'U':
            #under turn
            main_face = 4
            self.cube[0,2,:] = temp_cube[1,2,:]
            self.cube[3,2,:] = temp_cube[0,2,:]
            self.cube[5,0,:] = temp_cube[3,2,:]
            self.cube[1,:,2] = temp_cube[5,0,:]
        if turnType == 'T':
            #top turn
            main_face = 2
            self.cube[5,2,:] = temp_cube[1,0,:]
            self.cube[3,0,:] = temp_cube[5,2,:]
            self.cube[0,0,:] = temp_cube[3,0,:]
            self.cube[1,0,:] = temp_cube[0,0,:]
        temp_side = np.zeros((3,3),dtype=int)
        for i,x in enumerate(self.cube[main_face]):
            for j,y in enumerate(self.cube[main_face][i]):
                temp_side[i][j] = self.cube[main_face][(2-j)%3][i]
        self.cube[main_face] = temp_side
        #counter clockwise rotation?
        #cube[faces[0]][2][:] = temp_cube[faces[1]][:][2]
        #cube[faces[1]][:][0] = temp_cube[faces[2]][2][:]
        #cube[faces[2]][0][:] = temp_cube[faces[3]][:][0]
        #cube[faces[3]][:][2] = temp_cube[faces[0]][0][:]
        
        return(self.cube)

    def shuffle(self):
        l=['F','B','R','L','T','U']
        for x in range(20):
            i = random.randint(0,5)
            self.cube=self.rotate(l[i])
first=create_cube()
print(first.cube)
first.shuffle()
print('shuffled cube')
#first.cube = rotate(first.cube,'R')
print(first.cube)

