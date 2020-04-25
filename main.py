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
           255,
           255]
light = [[0.5,
          0.75,
          1],
         [255,
          255,
          255]]
areflect = [.1,
            .1,
            .1]
dreflect = [0,
            .5,
            0]
sreflect = [1,
            1,
            1]

screen = new_screen()
zbuffer = new_zbuffer()
color = [ 0, 255, 0 ]
edges = []
polygons = []
t = new_matrix()
ident(t)
csystems = [ t ]

parse_file( 'script', edges, polygons, csystems, screen, zbuffer, color, view, ambient, light, areflect, dreflect, sreflect)

screen = new_screen()
zbuffer = new_zbuffer()
color = [ 0, 255, 0 ]
edges = []
polygons = []
t = new_matrix()
ident(t)
csystems = [ t ]

parse_file( 'mypic', edges, polygons, csystems, screen, zbuffer, color, view, ambient, light, areflect, dreflect, sreflect)