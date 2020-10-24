int(input('Que distância vai percorrer? :'))
def preco_passagem(km):
    if km <= 200:
        km = km*0.5
        print('Sua viagem será: R${0:.2f}'.format(km))
    else:
        if km > 200:
            km = (200*0.5) + km*0.45
            print('Sua viagem será: R${0:.2f}'.format(km))