import math
def classifica_triangulo(a,b,c):
    if a == b and b == c and a == c:
        print("equilátero")
    elif a == b and a != c and b != c :
        print("isósceles")
    elif a == c and a != b and c != b:
        print("isósceles")
    elif b == c and b != a and c!= a:
        print("isósceles")
    else:         
        print("escaleno")
classifica_triangulo(1,2,4)