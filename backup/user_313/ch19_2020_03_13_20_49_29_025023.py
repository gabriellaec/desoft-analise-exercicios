def classifica_triangulo(a,b,c):
    if  (a+b)>c and (a+c)>b and (b+c)>a:
        return('Os lados fornecidos não formam um triangulo')

    elif a == b and a == c:
        return("equilátero")
    
    elif a != b and a != c and b != c :
        return("escaleno")

    else:
        return("isósceles")

