import math
def classifica_triangulo(a,b,c):
    if a == b and b == c and a == c:
        print("equilátero")
    elif a == b and a != c and b != c and b == a:
        print("isósceles")
    elif:         
        print("escaleno")
classifica_triangulo(1,2,4)