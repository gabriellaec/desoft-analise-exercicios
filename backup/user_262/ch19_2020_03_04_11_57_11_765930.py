def classifica_triangulo(a,b,c):
    if a==b==c:
        print("equilátero")
    if a==b!=c or b==c!=a or c==a!=b:
        print ("isóceles")
    if a!=c!=b:
        print("escaleno")