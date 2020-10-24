distancia = float(input("Qual a distânia que deseja percorrer em km?"))

if distancia <= 200:
    preco = distancia * 0,5
else:
    if (distancia * 0,5) >= (distancia * 0,45):
    	preco = distancia * 0,5
    else:
    	preco = distancia * 0,45

print("O valor da passagem é {0:.02f}.".format(preco))