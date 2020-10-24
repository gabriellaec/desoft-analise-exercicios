def classifica_triangulo(a, b, c): #lados do triângulo
    if a==b==c:
        return "equilátero"
    if a==b!=c or a==c!=b or b==c!=a:
        return "isósceles"
    if a!=b!=c:
        return "escaleno"