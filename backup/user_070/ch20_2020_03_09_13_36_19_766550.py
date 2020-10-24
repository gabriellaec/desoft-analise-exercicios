d=int(input('distancia em km?'))
if d<=200:
    print('R${0:.2f}'.format(d*0.5))
else:
    print('R${0:.2f}'.format(d*0.45))