def classifica_triangulo(a,b,c):
    if a==b==c:
        return "equilátero"
    if a!=b!=c:
        return "escaleno"
    else:
        return "isósceles"

x=10
y=10
z=10
print(classifica_triangulo(x,y,z)