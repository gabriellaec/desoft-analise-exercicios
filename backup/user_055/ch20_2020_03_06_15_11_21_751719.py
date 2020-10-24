int(input('Que distância vai percorrer?: '))
def preco_passagem(km):
    if km <= 200:
        km = km*0.5
    else:
        if km > 200:
            km = (200*0.5) + km*0.45
    print(km)