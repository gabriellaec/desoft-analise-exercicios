x = int(input('distancia a percorrer:       '))
z = 0
y = 0
if x < 200:
    z = x*(0.5)
if x > 200:
    y = 200*(0.5)+ (x-200)*0.45
