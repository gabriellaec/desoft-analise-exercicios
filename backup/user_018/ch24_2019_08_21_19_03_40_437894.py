def classifica_triangulo( a, b, c ):
    if (a==b and b==c):
        return 'Equilátero'
    if (a!=b and a!=c and b!=c):
        return 'Escaleno' 
    else:
        return 'Isósceles' 
    
a = int(input('Digite um lado do triângulo '))
b = int(input('Digite o segundo lado do triângulo '))
c = int(input('Digite o terceiro lado do triângulo '))

print (classifica_triangulo(a,b,c))