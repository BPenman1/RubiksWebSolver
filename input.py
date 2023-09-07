import string
import unittest
import itertools
import traceback
import eel

import cube as cube
from cube import Cube
from maths import Point, Matrix
from solve import Solver
from optimize import *
import optimize

# template for inputing cube configurtaion stringsYOYYOBOOO RGGWWWBOO BYB YGGWWWBBR BYY GRGWWWBGG YGY RRRBRORRO
#                        top
#                       {}{}{}
#                       {}{}{}
#                       {}{}{}
#                 left  front   right  back(is mirrored)
#                {}{}{} {}{}{} {}{}{} {}{}{}
#                {}{}{} {}{}{} {}{}{} {}{}{}
#                {}{}{} {}{}{} {}{}{} {}{}{}
#                       bottom
#                       {}{}{}
#                       {}{}{}
#                       {}{}{}
#just fill in empty spaces, select all except labels, and copy paste into one line string like below, all caps
#
#       c = Cube("OOOOOOOOOYYYWWWGGGBBBYYYWWWGGGBBBYYYWWWGGGBBBRRRRRRRRR")
#
#               this is what an already solved cube would look like inputed




#initialise web page for GUI
eel.init('GUI')

global directions


@eel.expose
def input_cube(cube_string):

    c = Cube(cube_string)
    #print (cube_string)
    solver = Solver(c)
    solver.solve()
    #print(solver.moves)
    solved = ', '.join(solver.moves)
    return solved


eel.start('index.html', mode=('chrome','edge'))
