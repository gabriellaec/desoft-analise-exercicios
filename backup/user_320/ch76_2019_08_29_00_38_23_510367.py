def aniversariantes_de_setembro(dados):
    aniver = {}
    for chave, valor in dados.items():
        data = valor.split('/')
        print(chave, data)
        if data[1] == '09':
            aniver[chave] = valor
    return aniver