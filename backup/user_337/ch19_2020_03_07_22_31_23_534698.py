def classifica_triangulo (a,b,c):
    if a == b and b == c:
        return 'o triangulo é equilátero'
    elif a == c != b or a == b != c or b == c != a:
        return 'o triangulo e isosceles'
    else:
        return 'o triangulo e escaleno'
