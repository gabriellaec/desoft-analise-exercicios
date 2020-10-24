from math import sin
from math import pi

def jaca(v, o):
    a = (o/180)*pi
    d = ((v**2)*(sin(2*a)))/9.8
    if d < 98:
        return("Muito perto")
    elif d >= 98 and d <=102:
        return("Acertou!")
    else:
        return("Muito longe")
    
    v = int(input("velocidade"))
    o = int(input("angulo em graus"))
    print(jaca(v, o))