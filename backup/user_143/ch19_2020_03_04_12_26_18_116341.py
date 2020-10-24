#Função que define triangulos
def classifica_triangulos(x, y, z):
    if x == y == z:
        print('equilatero')
    elif x == y != z or x != y == z:
        print('isosceles')
    else:
        print('escalenos')
        
