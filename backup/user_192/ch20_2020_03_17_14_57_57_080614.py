distancia = int(input('Qual distancia deseja percorrer? '))

if distancia <= 200:
    preco = distancia*0.50
else:
   preco = 100 + (distancia - 200)*0.45
   
print('O preco a se pagar e {:.2f}'.format(preco))