def verifica_idade(I):
    if I>=21:
        return 'Liberado Eua e Brasil'
    else:
        if I>=18:
            return 'Liberado Brasil'
        if I<18 and I>=0:
            return 'Nao esta liberado'