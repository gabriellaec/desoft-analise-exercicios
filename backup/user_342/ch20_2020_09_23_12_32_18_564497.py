resposta= float(input('qual distancia deseja percorrer em km?'))
if resposta<=200.00:
    preço= resposta*0.50
    texto='preço da viagem:{0:.2f}'.format(preço)
    print(texto)
else:
    preço= resposta*0.45
    texto='preço da viagem:{0:.2f}'.format(preço)
    print(texto)
