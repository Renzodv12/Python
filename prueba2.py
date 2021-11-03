"""
--------------------------------------------------------
|@                                                    |
|                                                      |
|                                                      |
|                                                      |
|                                                      |
|                                                      |
|                                                      |
|                                                      |
|                                                      |
|                                                      |
|                                                      |
--------------------------------------------------------
#if my_position[my_positionx] < 0:
#    my_position[my_positionx] = map_whidth
#elif my_position[my_positionx] >= map_whidth:
#    my_position[my_positionx] = 0
#elif my_position[my_positiony] < 0:
#    my_position[my_positiony] = map_heigth
#elif my_position[my_positiony] >= map_heigth:
#   my_position[my_positiony] = 0


map_objects=[[random.randint(0,map_whidth),random.randint(0,map_heigth)]
,[random.randint(0,map_whidth),random.randint(0,map_heigth)]
,[random.randint(0, map_whidth), random.randint(0, map_heigth)]
,[random.randint(0, map_whidth), random.randint(0, map_heigth)]
,[random.randint(0, map_whidth), random.randint(0, map_heigth)]
,[random.randint(0, map_whidth), random.randint(0, map_heigth)]
,[random.randint(0, map_whidth), random.randint(0, map_heigth)]
,[random.randint(0, map_whidth), random.randint(0, map_heigth)]
,[random.randint(0, map_whidth), random.randint(0, map_heigth)]
,[random.randint(0, map_whidth), random.randint(0, map_heigth)]]



def map():
    print("+" + "-" * (map_whidth * 3) + "+")
    for coordinate_y in range(map_heigth):
        print("|", end="")
        for coordinate_x in range(map_whidth):
            chart_to_draw = " "
            object_in_cell=None;
            for map_object in map_objects:
                if map_object[my_positionx] == coordinate_x and map_object[my_positiony] == coordinate_y:
                    chart_to_draw = "*"
                    object_in_cell = map_object
            if my_position[my_positionx] == coordinate_x and my_position[my_positiony] == coordinate_y:
                chart_to_draw = "@"
                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_length +=1
            print(" {} ".format(chart_to_draw), end="")
        print("|")
    print("+" + "-" * (map_whidth * 3) + "+")
     """
import os
import random
from readchar import readchar

my_position = [1, 0]
my_positionx = 0
my_positiony = 1
tail_length = 0


num_of_object = 10
map_objects = []
tail=[]
end_game = False
die = False
obstacle_definition = """\
       #         ##########################
                             #######       
###################        #####   ####### 
########################           ####### 
#################                             
########               #######        #### 
####################                       
######################         ############
####       ##########        #             
####       ##########        # # # # # #      
########     ###########         ############    
                             #######        
##############                             
########               #######        #### 
####################                       
       #         ##########################
####       ##########              ########\
"""


obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]
map_whidth = len(obstacle_definition[0])
map_heigth = len(obstacle_definition)
print(obstacle_definition[1][1])


def create_object(cant):
    while len(map_objects) < cant:
        new_position = [random.randint(0, map_whidth-1), random.randint(0, map_heigth-1)]
        if new_position not in map_objects and new_position != my_position and obstacle_definition[new_position[my_positiony]][new_position[my_positionx]] != "#":
            map_objects.append(new_position)


create_object(3)

while not end_game:
    print("+" + "-" * (map_whidth * 2) + "+")
    for coordinate_y in range(map_heigth):
        print("|", end="")
        for coordinate_x in range(map_whidth):
            chart_to_draw = "  "
            object_in_cell = None
            tail_in_cell = None
            create_object(3)
            for map_object in map_objects:
                if map_object[my_positionx] == coordinate_x and map_object[my_positiony] == coordinate_y:
                    chart_to_draw = " *"
                    object_in_cell = map_object
            for tail_piece in tail:
                if tail_piece[my_positionx] == coordinate_x and tail_piece[my_positiony] == coordinate_y:
                    chart_to_draw = " @"
                    tail_in_cell = tail_piece
            if my_position[my_positionx] == coordinate_x and my_position[my_positiony] == coordinate_y:
                chart_to_draw = " @"
                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_length += 1
                if tail_in_cell:
                    chart_to_draw = "GAME OVER"
                    end_game = True
                    die = True
            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                if chart_to_draw != " *":
                    chart_to_draw = " #"
            print("{}".format(chart_to_draw), end="")
        print("|")
    print("+" + "-" * (map_whidth * 2) + "+")
    print("Tamaño de la cola {}".format(tail))
    print("Cant de la object {}".format(len(map_objects)))
    print(" object {}".format(map_objects))

    direction = readchar().decode()
    #print(direction)

    new_position=None
    if direction == "w":
        new_position = [my_position[my_positionx], int((my_position[my_positiony] - 1) % map_heigth)]
    elif direction == "s":
        new_position = [my_position[my_positionx],int((my_position[my_positiony] + 1) % map_heigth)]
    elif direction == "a":
        new_position = [int((my_position[my_positionx] - 1) % map_whidth),my_position[my_positiony]]
    elif direction == "d":
        new_position = [int((my_position[my_positionx]+ 1) % map_whidth),my_position[my_positiony]]
    elif direction == "x":
        end_game = True
    os.system('cls')

    if new_position:
        if obstacle_definition[new_position[my_positiony]][new_position[my_positionx]] != "#":
            tail.insert(0, my_position.copy())
            tail = tail[:tail_length]
            my_position = new_position


if die:
    print("Has muerto")



