import math
def calcula_trabalho():
    F=int(input('F?:'))
    a=int(input('O?:'))
    b=math.radians(a)
    s=int(input('s?:'))
    t= F*math.cos(b)*s
    J=t*s
    print(J)
