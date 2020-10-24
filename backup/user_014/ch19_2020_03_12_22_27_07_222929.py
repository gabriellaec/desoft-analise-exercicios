def classifica_triangulo (a, b, c):
    if a != b and b != c and c != a:
        print('escaleno')
    elif a == b or b == c or c == a:
        print('isóceles')
    elif a == b and b == c and c == a:
        print ('equilátero')