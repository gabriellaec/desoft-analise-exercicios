   def ola(x, y, z):
    if (x == y and x != z and y != z) or (x == z and x != y and z != y) or (y == z and y !=x and z !=x):
        return("isóceles")
    elif y != x and x != z and y != z :
        return("escaleno")
    else:
        return("equilátero")
print(ola(3, 1, 3))