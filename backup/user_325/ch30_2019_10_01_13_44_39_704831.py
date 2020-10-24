from math import sin
from math import pi

def jaca(v, o):
    a = (o/180.0)*pi
    d = ((v**2.0)*(sin(2.0*a)))/9.8
    if d < 98.0:
        return("Muito perto")
    elif d >= 98.0 and d <=102.0:
        return("Acertou!")
    else:
        return("Muito longe")
    
    v = float(input("velocidade"))
    o = float(input("angulo em graus"))
    print(jaca(v, o))