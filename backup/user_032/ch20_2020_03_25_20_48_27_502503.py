def preço_da_viagem(distancia):
    if distancia <=200:
        return 'O preço da passagem é R$ {0:.2f}'.format(distancia*0.5)
    else:
        return 'O preço da passagem é R$ {0:.2f}'.format(100+((distancia-200)*0.45))
distancia = int(input('Qual a distancia percorrida?'))
print(preço_da_viagem(distancia))