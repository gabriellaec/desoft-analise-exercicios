def verifica_idade(idade):
    if idade >= 21:
        return 'Liberado_EUA_e_BRASIL'
    elif idade >= 18:
        return 'Liberado_BRASIL'
    else:
        return 'Não está liberado'
