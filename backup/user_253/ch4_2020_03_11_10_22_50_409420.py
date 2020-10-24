def classifica_idade(idade):
    if idade <=11:
        return 'crianca'
    if idade>11 and idade < 17:
        return ('adolecente')
    else:
        return ('adulto')