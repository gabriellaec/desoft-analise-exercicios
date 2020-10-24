#Função que define triangulos
def classifica_triangulo(x, y, z):
    if x == y and x == z and y == z:
        return equilatero
    elif x==y or x==z or y==z:
        return isosceles
    else:
        return escaleno

        
