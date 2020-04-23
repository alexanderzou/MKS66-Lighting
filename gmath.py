import math
from display import *


  # IMPORANT NOTE

  # Ambient light is represeneted by a color value

  # Point light sources are 2D arrays of doubles.
  #      - The fist index (LOCATION) represents the vector to the light.
  #      - The second index (COLOR) represents the color.

  # Reflection constants (ka, kd, ks) are represened as arrays of
  # doubles (red, green, blue)

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 4

#lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
    normalize(normal)
    normalize(light[0])
    normalize(view)
    amb = calculate_ambient(ambient, areflect)
    dif = calculate_diffuse(light, dreflect, normal)
    spe = calculate_specular(light, sreflect, view, normal)
    r = limit_color(amb[0]) + limit_color(dif[0]) + limit_color(spe[0])
    g = limit_color(amb[1]) + limit_color(dif[1]) + limit_color(spe[1])
    b = limit_color(amb[2]) + limit_color(dif[2]) + limit_color(spe[2])
    return [r, g, b]

def calculate_ambient(alight, areflect):
    rAmb = alight[0] * areflect[0]
    gAmb = alight[1] * areflect[1]
    bAmb = alight[2] * areflect[2]
    return [rAmb, gAmb, bAmb]

def calculate_diffuse(light, dreflect, normal):
    dot = dot_product(light[0], normal)
    rDif = light[1][0] * dreflect[0] * dot
    gDif = light[1][1] * dreflect[1] * dot
    bDif = light[1][2] * dreflect[2] * dot
    return [rDif, gDif, bDif]

def calculate_specular(light, sreflect, view, normal):
    #print('---')
    bracket = max(0, dot_product(light[0], normal))
    #print(bracket)
    bracket = vectConst(normal, 2*bracket)
    #print(bracket)
    bracket = vectSub(bracket, light[0])
    #print(bracket)
    bracket = dot_product(bracket, view)
    #print(bracket)
    bracket = bracket ** 5
    #print(bracket)
    rSpe = light[1][0] * sreflect[0] * bracket
    gSpe = light[1][1] * sreflect[1] * bracket
    bSpe = light[1][2] * sreflect[2] * bracket
    return [rSpe, gSpe, bSpe]

def limit_color(color):
    if color < 0:
        return 0
    elif color > 255:
        return 255
    else:
        return int(color)

#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    magnitude = math.sqrt( vector[0] * vector[0] +
                           vector[1] * vector[1] +
                           vector[2] * vector[2])
    for i in range(3):
        vector[i] = vector[i] / magnitude

#Return the dot porduct of a . b
def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N

#Vector subtraction
def vectSub(v1, v2):
    return [v1[0]-v2[0], v1[1]-v2[1], v1[2]-v2[2]]
    
#Vector multiplication by a constant
def vectConst(v, c):
    return [c*v[0], c*v[1], c*v[2]]