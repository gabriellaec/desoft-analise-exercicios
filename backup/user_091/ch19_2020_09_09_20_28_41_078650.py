def classifica_triangulo(a,b,c):
    if a==b  and b==c:
        return "equilátero"
    elif a==b or b==c or a==c:
        return "isósceles"
    else:
        if a!=b and a!=c:
            return "escaleno"

x=10
y=10
z=10
print(classifica_triangulo(x,y,z)