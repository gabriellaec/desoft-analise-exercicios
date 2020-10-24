def verifica_idade(idade):
    if 21> idade >= 18:
        return 'Liberado BRASIL'
    else:
        if idade >= 21:
            return 'Liberada EUA e BRASIL'
        else:
            return 'Não está liberado'