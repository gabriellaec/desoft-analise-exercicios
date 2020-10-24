distancia = flot(input('Qual a distancia da viagem em km?'))
if distancia <= 200:
    passagem=0.5*distancia
    
else:
    passagem = 100+0.45*(distancia-200)
print('Preço da passagem=R${0:2f}'.format(passagem))