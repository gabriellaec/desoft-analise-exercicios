import math
def calcula_trabaho(f, teta, s):
    a=math.radians(teta)
    b=math.cos(a)
    trabalho=f*b*s
    return trabalho