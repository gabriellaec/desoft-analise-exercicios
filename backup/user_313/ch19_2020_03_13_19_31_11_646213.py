def classifica_triangulo(a,b,c):


    if a == b and a == c:
        print("equilátero")
    
    elif a != b and a != c and b != c :
        print("escaleno")

    else:
        print("isósceles")
