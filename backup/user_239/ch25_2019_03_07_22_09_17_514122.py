distancia=float(input('Qual a distância em km?'))
y=(distancia*1/2)
z=(distancia*45/100)+100
y=round(y,2)
z=round(z,2)
if distancia<200:
    print (y)
else:
    print (z)
