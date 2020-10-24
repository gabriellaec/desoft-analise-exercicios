def verifica_idade(I):
    if I>=21:
        return 'Liberado Eua e Brasil'
    elif I>=18:
        return 'Liberado Brasil'
    if I<18 and I>=0:
        return 'Não está liberado'