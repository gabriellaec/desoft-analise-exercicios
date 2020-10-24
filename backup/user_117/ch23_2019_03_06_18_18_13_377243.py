def verifica_idade(idade):
    if int(idade)>=18 and int(idade)<21:
        return 'Liberado BRASIL'
    elif int(idade)>=21:
        return 'Liberado EUA e BRASIL'
    else:
        return 'Não está liberado'