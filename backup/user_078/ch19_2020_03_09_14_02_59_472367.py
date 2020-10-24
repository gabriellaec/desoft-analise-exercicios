def classifica_triangulo (a,b,c):
    if a==b and b==c :
        return ('triângulo equilátero')
    elif a==b or a==c or b==c:
        return ('triângulo isósceles')
    else:
        return ('triângulo escaleno')