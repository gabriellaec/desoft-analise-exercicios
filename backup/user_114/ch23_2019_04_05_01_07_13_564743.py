def verifica_idade(I):
    if I>=21:
        return 'Liberado EUA e Brasil'
    elif I>=18:
        return 'Liberado Brasil'
    else:
        return 'Não está liberado'