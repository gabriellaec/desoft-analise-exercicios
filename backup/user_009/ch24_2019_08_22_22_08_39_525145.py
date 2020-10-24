def classifica_triangulo(a,b,c):
    if a == b  and b == c and abs(a-b) < c and abs(a-b) < a + b:
        return 'equilátero'
    elif a == b and b != c or a != b and b == c or c == a and c!= b and abs(a-b) < c and abs(a-b) < a + b:
        return 'isóceles'
    elif a !=b and a!= c and b != c:
        return 'escaleno'