import math
def calcula_elongacao(A, faseinicial, w, t):
    x= A*math.cos(math.radians(faseinicial)+math.radians(w)*t)
    return x