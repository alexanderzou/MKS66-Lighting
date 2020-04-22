from display import *
from draw import *
from parse import *
from matrix import *
import math


# lighting values
view = [0,
        0,
        1];
ambient = [255,
           0,
           255]
light = [[0.5,
          0.75,
          1],
         [0,
          255,
          255]]
areflect = [1,
            1,
            1]
dreflect = [0,
            0,
            0]
sreflect = [0,
            0,
            0]



screen = new_screen()
zbuffer = new_zbuffer()
color = [ 0, 255, 0 ]
edges = []
polygons = []
t = new_matrix()
ident(t)
csystems = [ t ]


parse_file( 'script', edges, polygons, csystems, screen, zbuffer, color, view, ambient, light, areflect, dreflect, sreflect)
