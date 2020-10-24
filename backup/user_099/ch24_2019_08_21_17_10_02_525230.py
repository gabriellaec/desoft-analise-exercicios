def classifica_triangulo(a,b,c):
    if a==b and b==c:
        return("Triângulo equilátero")
    elif a==b or b==c or a==c:
        return("Triângulo isósceles")
    else:
        return("Triângulo escaleno")
