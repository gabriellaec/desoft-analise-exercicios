def testa_maioridade(idade):
    if idade >= 21:
        return 'Maior nos EUA e BRASIL'
    else:
        if idade >= 18:
            return 'Maior no BRASIL'
        else:
            return 'Menor de idade'