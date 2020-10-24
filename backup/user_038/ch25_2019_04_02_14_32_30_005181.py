distancia = int(input("Qual a distancia que voce deseja percorrer: "))
if distancia<=200:
    passagem = distancia*0.5
elif distancia>200:
	passagem = (distancia-200)*0.45 + 200*0.5
print(round(passagem,2))