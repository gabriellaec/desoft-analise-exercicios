def classifica_triangulo (a,b,c):
    if (a==b and a==c):
        return ("Triângulo equilátero")
    elif ((a==b and a!=c) or (a!=b and a==c) or b==c):
        return ("Triângulo isóceles")
    else:
        return ("Triângulo escaleno")
