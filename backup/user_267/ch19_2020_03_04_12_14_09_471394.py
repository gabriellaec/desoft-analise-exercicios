x = float(input('Valor do lado x:')
y = float(input('Valor do lado y:')
z = float(input('Valor do lado z')
          
def lados(x, y, z)

if x == y and x == z:
    print("equilátero")

else:
    if x == y or x == z or y == z:
        print("isósceles")

else:
    print("escaleno")