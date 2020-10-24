def classifica_triangulo(a,b,c):
    if not (a+b)>c and (a+c)>b and (b+c)>a:
        print('Os lados fornecidos não formam um triangulo')

    if a == b and a == c:
        print("equilátero")
    
    elif a != b and a != c and b != c :
        print("escaleno")

    else:
        print("isósceles")
