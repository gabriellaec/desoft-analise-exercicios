d = float(input(distancia))
def preco_passagem(d):
    if d<=200:
        p=d*0.5
        return p
    else:
        p=(d-200)*0.45+100
        return p
print('Preco da passagem: R${0:.2f}'.format(preco_passagem(d)))

