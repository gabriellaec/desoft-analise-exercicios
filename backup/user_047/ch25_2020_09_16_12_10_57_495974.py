import math
def jacawars(angulo,v):
    raio = 2
    d = (v**2*math.sin(angulo))/9.8
    if d+r>=98 and d+r<100:
        return 'Muito perto'
    if d+r>100:
        return 'Muito longe'