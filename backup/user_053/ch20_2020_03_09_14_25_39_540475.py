distancia=int(input('Digite sua distância: '))

if distancia<=200:
    preco=0.50*distancia
else:
    preco=0.50*200+0.45*(distancia-200)
    
print('O preço é de R$ {0:.2f}'.format(preco))