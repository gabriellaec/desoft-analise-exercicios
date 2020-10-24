def passagem(km):
    km=int(input("Qtos km vc rodou? ")
    if km <= 200:
        preco = 0.50*km
    elif km > 200:
        preco = 0.45*(km-200)+0.50*km
    return preco

print(passagem(km))

    