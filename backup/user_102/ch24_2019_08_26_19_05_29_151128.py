def triangle(x, y, w):
    if x == y and x == w:
        return "equilátero"
    elif x == y and x != w and y != w:
        return "isósceles"
    else:
        return "escaleno"
d = int(input())
f = int(input("Numero: "))
g = int(input("Numero: "))

print(triangle(d, f, g))