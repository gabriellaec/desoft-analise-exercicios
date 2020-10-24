def classifica_triangulo(x,y,z):
    if x==y==z:
        print("seu triângulo é equilátero")
    elif x!=y!=z:
        print("seu triângulo é escaleno")
    else:
        print("seu triângulo é isóceles")
    return
classifica_triangulo(1,1,1)
