km = int(input('Que distância vai percorrer?: '))
def preco_passagem(km):
    if km <= 200:
        preco = (km*0.5)
    elif km > 200:
        preco = (200*0.5) + km*0.45
    print(preco)