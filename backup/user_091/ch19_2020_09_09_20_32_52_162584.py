def classifica_triangulo(a,b,c):
    if a==b  and b==c:
        return "equilátero"
    elif a==b or b==c or a==c:
        return "isósceles"
    else:
        if a!=b and a!=c:
            return "escaleno"

x=str(input('insira um numero: ')
y=str(input('insira um outro numero: ')
z=str(input('insira outro numero:  ')

print(classifica_triangulo(x,y,z))