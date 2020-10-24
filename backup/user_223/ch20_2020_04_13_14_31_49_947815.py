distancia=int(input("Insira a distancia que você deseja percorrer:"))
if distancia<=200:
    preco_passagem=distancia*0.5
else:
    preco_passagem=200*0.5+(distancia-200)*0.45
print(preco_passagem)