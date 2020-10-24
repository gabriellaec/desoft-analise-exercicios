#Equilatero = lados iguais
#Isóceles = 2 lados iguais e 1 diferente
#Escaleno = lados diferentes

def classifica_triangulo (a,b,c):
    if a == b and a == c and b ==c:
        return ('equilátero')
    elif a != b and a!= c and b != c:
        return ('escaleno')
    else:
        return ('isósceles')
  
