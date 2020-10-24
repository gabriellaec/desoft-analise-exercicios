def preco_da_viagem(d):
    if distancia <= 200:
        return 'O preço da sua viagem é R${0:.2f}'.format(d*0.5)
    else:
        return 'O preço da sua viagem é R${0:.2f}'.format(100+((d-200)*0.45))
  
distancia = int(input('Qual a distância a percorrer desejada?: (km)'))
print (preco_da_viagem(d))
                