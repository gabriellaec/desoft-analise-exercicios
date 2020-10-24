distancia = int(input('Qual a distância que você deseja percorrer? ')
distancia_maior = 200 + (distancia - 200)
       
if distancia < 200:
   preço = distancia * 0.50
else:
   preço = distancia * 0.50 + distancia_maior * 0.45
        
print(preço)