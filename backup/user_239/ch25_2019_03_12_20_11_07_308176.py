distancia=float(input('Qual a distância em km?'))
if distancia<=200:
    custo=0.5*distancia
else:
    custo=200*0.5+(distancia-200)*0.45
print("{0:.2f} reais".format(custo))