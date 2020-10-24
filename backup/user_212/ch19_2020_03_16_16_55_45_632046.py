def tipo_triângulo (x,y,z):
    if x == y == z:
        print ("é equilátero")
    elif x == y and x == z and y == z:
        print (" é isóceles")
    else:
        print ("é esscaleno")