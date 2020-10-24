# Exercicio 4
def preco_da_passagem(km):
    if km <= 200:
        preco = km*(0.5)
        return preco
    elif km > 200:
        preco = 100 + (km-200)*(0.45)
        return preco
a = int(input('Insira a distância da viagem em km: '))
print("O preço é {0:.2f}" .format (preco_da_passagem(a)))