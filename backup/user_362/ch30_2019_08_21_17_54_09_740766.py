import math
def Jaca_Wars(v,o):
    d=((v**2)*(math.sin(2*o)))/9.8
    print(d)
    if d > 102:
        return("Muito longe")
    elif d < 98:
        return ("Muito perto")
    else:
        return("Acertou!")

