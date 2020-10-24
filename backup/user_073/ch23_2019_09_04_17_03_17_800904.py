def verifica_idade(idade):
    if idade>=21:
        return 'liberado EUA e Brasil'
    if idade<18:
        return 'nao esta liberado'
    else:
        return 'esta liberado Brasil'


  