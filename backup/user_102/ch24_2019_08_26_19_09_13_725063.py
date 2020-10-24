
d = int(input())
f = int(input("Numero: "))
g = int(input("Numero: "))

def triangle(x, y, w):
    if x == y and x == w:
        return "equilátero"
    elif x == y and x != w and y != w:
        return "isósceles"
    else:
        return "escaleno"


print(triangle(d, f, g))