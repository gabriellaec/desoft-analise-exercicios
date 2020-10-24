import math
def classifica_triangulo(a,b,c):
    if a == b == c :
        print("equilátero")
    elif a == b and a != c and b != c:
        print("isósceles")
    else:
        print("escaleno")
classifica_triangulo(1,2,4)