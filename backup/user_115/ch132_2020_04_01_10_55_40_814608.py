
# trabalho
# t = f * cos(theta) * s
# f (force), theta (angle), s (distance)
#return t in joules

import math

def calcula_trabalho(f, theta, s):
    theta = theta*(180/math.pi)
    t= f*math.cos(theta)*s
    return t
