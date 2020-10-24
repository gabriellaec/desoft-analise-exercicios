distancia=int(input('Qual a distância do trajeto? '))

def preco(distancia):
    if distancia > 200:
       return 100+(distancia-200)*0.45
    else:
       return distancia*0.5
print ("{0:.2f}".format(preco(distancia)))