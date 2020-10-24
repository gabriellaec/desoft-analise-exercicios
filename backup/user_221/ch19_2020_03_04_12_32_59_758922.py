def testa_x_y_z(x,y,z):
    if x==y and x==z:
        print ('equilatero')
    elif x==y and x!=z:
        print('isosceles')
    else:
        print('escaleno')
print(testa_x_y_z(3,4,5))
print(testa_x_y_z(3,3,3))