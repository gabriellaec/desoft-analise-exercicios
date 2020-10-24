distancia = float(input('Qual a distância da viagem em km?'))
if distancia <= 200:
    passagem = 0.5 * distancia
    print ('preço por quilometro = R$0.50')
else:
    passagem = 100 + 0.45 * (distancia - 200)
    print ('preço por quilometro = R$0.45')
print("Preço da passagem = R${0}".format(passagem))