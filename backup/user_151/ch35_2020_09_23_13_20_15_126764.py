x = True
z = 0
while x:
    y = int(input('Numeros'))
    if y != 0:
        z = z + y
    else:
        x = False
        
print(z)