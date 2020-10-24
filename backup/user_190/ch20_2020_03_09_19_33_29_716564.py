d= int(input('quantos km deseja viajar? '))
if d<=200:
    print (0.50*d)
else:
    print ((0.50*d)+(0.45*(d-200)))