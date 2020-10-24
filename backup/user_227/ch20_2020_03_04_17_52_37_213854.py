distancia = float(input("Qual a distância que você quer percorrer? "))
if distancia < 200:
   preco_da_passagem = distancia*0.5
else:
   preco_da_passagem = (distancia - 200)*0.45 + 100
print("Preco da passagem: R${0}".format(preco_da_passagem))