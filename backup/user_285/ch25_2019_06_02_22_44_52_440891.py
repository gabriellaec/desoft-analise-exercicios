distancia= int(input("Qual a distância que você deseja percorrer em km? ")
if distancia<=200:
               preco= distancia*0.5
else: 
               preco=200*0.5 + (distancia-200)*0.45
print("O preço é de {0}".format(preco))