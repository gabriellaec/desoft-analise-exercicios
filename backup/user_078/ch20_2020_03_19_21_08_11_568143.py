distancia=float(input('Distância que deseja percorrer: '))
if distancia<=200:
    print ('R${0:.2f}'.format(distancia*0.50))
else:
    print ('R${0:.2f}'.format((distancia*0.50)+(distancia-200)*0.45)