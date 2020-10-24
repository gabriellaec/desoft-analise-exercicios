def testa_maioridade(idade):
    if idade >= 21:
        return 'Maior nos EUA e Brasil'
    elif idade >= 18:
        return 'Maior no Brasil'
    else:
        return 'Menor de idade'
print(testa_maioridade(17))
print(testa_maioridade(20))
print(testa_maioridade(21))