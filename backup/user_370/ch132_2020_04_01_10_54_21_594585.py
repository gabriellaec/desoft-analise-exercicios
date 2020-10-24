from math import radians
from math import cos

def calcula_trabalho (F,theta,s):
    conv_rad= radians (theta)
    trabalho= F * cos(conv_rad)*s
    return trabalho