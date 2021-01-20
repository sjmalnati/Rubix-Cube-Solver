#rubix cube solver
#0 is front
#1 is R
#2 is Top
#3 is L
#4 is Bottom
#5 is Under

def rotate(cube, turnType):
    if turnType == 'F':
        #front turn
        
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

#rubix cube solver

class create_cube():
    def __init__(self):
        self.cube=[[[i]*3]*3 for i in range(6)]

first=create_cube()
print(first.cube)
