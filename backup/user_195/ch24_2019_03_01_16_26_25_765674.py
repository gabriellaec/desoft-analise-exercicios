def classifica_triangulo(a,b,c):
    if a==b and b==c:
        print ("equilatero")
    elif a!=b and b!=c and a!=c:
        print("escaleno")
    else:
        print ("isosceles")