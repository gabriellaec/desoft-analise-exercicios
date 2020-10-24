def verifica_idade(idade):
    if idade >=21:
        return 'Liberado EUA e BRASIL'
    if  18<=idade<20:
        return 'Liberado BRASIL'
    else:
        return 'Não está liberado'
        
        