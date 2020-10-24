distancia = int(input("Qual a distância em km você deseja percorrer?  "))
          
preco1 = distancia * 0.50
diferenca = distancia - 200
extra = diferenca * 0.45 + 100
                
                
if distancia <= 200:
       print("Valor {0:.2f}".format(preco1))
else:
       print("Valor {0:.2f}".format(extra))