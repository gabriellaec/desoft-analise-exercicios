a = int(input('Insira o lado a '))
b = int(input('Insira o lado b '))
c = int(input('Insira o lado c '))
def tipo_de_triangulo(a,b,c):
    if a == b and a == c:
        print('O triângulo é equilátero')
        return 'equilatero'
    elif a==b or a==c or b==c:
        print ('O triângulo é isósceles')
        return 'isósceles'
    else:
        print('O triângulo é escaleno')
        return 'escaleno'
tipo_de_triangulo(a,b,c)