def triangle(x, y, w):
    if x == y and x == w:
        return "equilatero"
    elif x == y and x != w and y != w:
        return "Isosceles"
    else:
        return "escaleno"


d = int(input("Numero: "))
f = int(input("Numero: "))
g = int(input("Numero: "))

print(triangle(d, f, g))