distancia = int(input("Qual a distancia que voce deseja percorrer: "))
passagem = distancia*0.5
if distancia>200:
	passagem += (distancia-200)*0.45
print(round(passagem,2))