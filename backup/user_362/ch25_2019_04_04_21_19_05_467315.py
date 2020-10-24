def passagem(km):
    if km <= 200:
        preco = 0.50*km
	elif km > 200:
        preco = 0.45*(km-200)+0.50*km
	return preco
km=int(input("Qtos km vc rodou? ")
print(passagem(km))