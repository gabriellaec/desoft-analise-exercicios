def testa_maioridade (idade):
    if idade >=21:
        return 'Maior de idade nos EUA e Brasil'
    else:
        if idade >= 18:
            return 'Maior de idade no Brasil'
        else:
            return 'Menor de idade'
print (testa_maioridade(17))
print (testa_maioridade(18))
print (testa_maioridade(21))