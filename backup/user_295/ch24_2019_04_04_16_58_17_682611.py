def classifica_triangulo (a, b, c):
    if a==b==c: 
        return ("equilátero")
    elif a == b or a ==c or b == a:
        return ("isósceles")
    else: 
        return ("escaleno") 
        