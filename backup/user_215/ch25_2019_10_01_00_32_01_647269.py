distancia = float(input("Quantos km voce pretende viajar")

	if distancia <= 200:
                preco = distancia * 0.5
                print(f"O preço da sua passagem é de R${preco:.2f}")
	elif distancia > 200:
                preco = 100 + ((distancia - 200) * 0.45)
                print(f"O preço da sua passagem é de R${preco:.2f}")