def preco_passagem(d):
    if d <= 200 :
        preco = d * 0.5
    else:
        preco = 100 + ((d-200) * 0.45)
    return preco


dist = float(input("Distância da Viagem: "))
print({0:.2f}.format(preco_passagem(dist)))