distancia = float(input('Qual a distância que você deseja percorrer? ')
       
if (distancia < 200):
   preço = distancia * 0.50
else:
   distancia_maior = 200 + (distancia - 200)
   preço = distancia * 0.50 + distancia_maior * 0.45
        
print('O preço da passagem é: R$ {0:.2f}'.format(preço))