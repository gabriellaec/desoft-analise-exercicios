import math
def jaca(v, o):
    d = (((v**2.0)*math.sin(2.0*o))/9.8)
    if d < 98.0:
        return ("Muito perto")
    elif d >= 98.0 and d <= 102.0:
        return ("Acertou!")
    else:
        return ("Muito longe")
print(jaca(5.0, 45.0))