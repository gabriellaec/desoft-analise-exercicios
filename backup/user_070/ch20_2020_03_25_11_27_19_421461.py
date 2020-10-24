d=int(input('distancia em km?'))
if d<=200:
    print('R${0}'.format(d*0.5))
else:
    print('R${0}'.format((d-200)*0.45+100))