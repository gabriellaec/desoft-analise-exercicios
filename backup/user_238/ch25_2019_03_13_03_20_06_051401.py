def preco(distancia):
    if distancia<=200:
        passagem=0.5*distancia
    else:
        passagem=100+0.45*(distancia-200)
    return passagem
distancia=int(input('que distancia vc quer percorrer? ')
print(preco(distancia))