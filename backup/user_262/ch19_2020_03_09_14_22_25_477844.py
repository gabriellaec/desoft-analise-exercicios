def classifica_triangulo(a,b,c):
    if a==b==c:
        print("equilátero")
    elif a==b!=c or b==c!=a or c==a!=b:
        print ("isóceles")
    else a!=c!=b:
        print("escaleno")