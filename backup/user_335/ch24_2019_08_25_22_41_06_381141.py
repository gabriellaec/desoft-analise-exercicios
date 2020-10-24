def classifica_triangulo (a,b,c):
    if (a==b and a==c):
        return ("Triângulo equilátero")
    elif ((a==b and a!=c) or (a!=b and a==c) or b==c):
        return ("Triângulo isóceles")
    else:
        return ("Triângulo escaleno")
    
x = int(input("Digite o valor para um lado do triângulo: "))
y = int(input("Digite outro valor para outro lado do triângulo: "))
z = int(input("Digite um valor para o último lado do triângulo: "))

r = (classifica_triangulo (x,y,z))
print (r)