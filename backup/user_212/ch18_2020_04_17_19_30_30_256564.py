def verifica_idade (idade):
    if (idade == 18) or (idade> and idade <21):
        return 'Liberado BRASIL'
    if idade < 18:
        return 'Não está liberado'
    else:
        return 'Liberado EUA e BRASIL'