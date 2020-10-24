def preco(km):
    if km <= 200:
        reais = 0.5*km
    else:
        reais = 100 + 0.45*(km-200)
    return reais

a=float(input('Quantos quilômetros você deseja viajar?: '))

print(preco(a))