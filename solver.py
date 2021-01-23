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
    
    def rotate(self,cube,turnType):
        temp_cube = copy.deepcopy(cube)
        if turnType == 'F':
            #front
            main_face = 0
            cube[2,2,:] = temp_cube[1,:,2]
            cube[3,:,0] = temp_cube[2,2,:]
            cube[4,0,:] = temp_cube[3,:,0]
            cube[1,:,2] = temp_cube[4,0,:]
        if turnType == 'R':
            #right turn
            main_face = 1
            cube[2,:,2] = temp_cube[0,:,2]
            cube[5,:,2] = temp_cube[2,:,2]
            cube[4,:,2] = temp_cube[5,:,2]
            cube[0,:,2] = temp_cube[4,:,2]
        if turnType == 'L':
            #left turn
            main_face = 3
            cube[2,:,0] = temp_cube[5,:,0]
            cube[0,:,0] = temp_cube[2,:,0]
            cube[4,:,0] = temp_cube[0,:,0]
            cube[5,:,0] = temp_cube[4,:,0]
        if turnType == 'B':
            #back turn
            main_face = 5
            cube[4,2,:] = temp_cube[1,:,0]
            cube[3,2,:] = temp_cube[4,2,:]
            cube[2,0,:] = temp_cube[3,2,:]
            cube[1,:,0] = temp_cube[2,0,:]
        if turnType == 'U':
            #under turn
            main_face = 4
            cube[0,2,:] = temp_cube[1,2,:]
            cube[3,2,:] = temp_cube[0,2,:]
            cube[5,0,:] = temp_cube[3,2,:]
            cube[1,:,2] = temp_cube[5,0,:]
        if turnType == 'T':
            #top turn
            main_face = 2
            cube[5,2,:] = temp_cube[1,0,:]
            cube[3,0,:] = temp_cube[5,2,:]
            cube[0,0,:] = temp_cube[3,0,:]
            cube[1,0,:] = temp_cube[0,0,:]
        temp_side = np.zeros((3,3),dtype=int)
        for i,x in enumerate(cube[main_face]):
            for j,y in enumerate(cube[main_face][i]):
                temp_side[i][j] = cube[main_face][(2-j)%3][i]
        cube[main_face] = temp_side
        #counter clockwise rotation?
        #cube[faces[0]][2][:] = temp_cube[faces[1]][:][2]
        #cube[faces[1]][:][0] = temp_cube[faces[2]][2][:]
        #cube[faces[2]][0][:] = temp_cube[faces[3]][:][0]
        #cube[faces[3]][:][2] = temp_cube[faces[0]][0][:]
        
        return(cube)
    def shuffle(self):
        l=['F','B','R','L','T','U']
        for x in range(3):
            i = random.randint(0,5)
            self.cube=self.rotate(self.cube,l[i])
            print('turn: ',l[i])

    def Breadth_solve(self):
        import time
        #breadth first search
        queue = []
        visited = {}
        queue.append(self.cube)
        l=['F','B','R','L','T','U']
        solved = create_cube()
        solved = solved.cube
        while queue:
            curr = queue.pop(0)
            for t in l:
                temp = copy.deepcopy(curr)
                turn = self.rotate(temp,t)
                currhash=turn.tobytes()
                
                if (turn == solved).all():
                    #print(turn)
                    print('found solution')
                    self.cube=turn
                    return 
                if(currhash not in visited):
                    queue.append(turn)
                    
                else:
                    pass
                    #print('Turn: ',t)
                    #print(turn)
                    #time.sleep(5)
                    #print(visited)
                visited[currhash]=1
        return
    def metric(self,cube):
        dist = 0
        for face in cube:
            vect1 = [1,0,-1]
            vect2 = [1,-1,0]
            vect3 = [0,1,-1]
            for row in face:
                if not row.dot(vect1) == 0:
                    dist+=1
                if not row.dot(vect2) == 0:
                    dist+=1
                if not row.dot(vect3) == 0:
                    dist+=1
            for col in face.T:
                if not col.dot(vect1) == 0:
                    dist+=1
                if not col.dot(vect2) == 0:
                    dist+=1
                if not col.dot(vect3) == 0:
                    dist+=1
        return(dist)
            
                
    
    def create_tests(self,n):
        tests=[]
        level=[]
        i=0
        tests.append([create_cube().cube])
        l=['F','B','R','L','T','U']
        visited = {}
        for testcase in range(1,n+1):
            tests.append([])
            for subcase in tests[i]:
                currhash=subcase.tobytes()
                visited[currhash]=1
                for turn in l:
                    temp = copy.deepcopy(subcase)
                    temp = self.rotate(temp,turn)
                    currhash=temp.tobytes()
                    if(currhash not in visited):
                        tests[i+1].append(temp)
                    
            i+=1
        return tests    
'''
first=create_cube()
#print(first.cube)
first.shuffle()
print(first.metric(first.cube))
#print('shuffled cube')
#first.cube = rotate(first.cube,'R')
print(first.cube)
first.Breadth_solve()
print(first.cube)
#print(first.cube)
#first.Breadth_solve()
#print(first.cube)
print('shuffled cube')
print(first.cube)
first.Breadth_solve()
print(first.cube)
'''
first=create_cube()
test=first.create_tests(3)
print(len(test[3]))
