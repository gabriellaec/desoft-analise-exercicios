def classifica_triangulo (x,y,z):
    if x == y == z:
        print ("é equilátero")
    elif x == y or x == z or y == z:
        print (" é isóceles")
    else:
        print ("é esscaleno")