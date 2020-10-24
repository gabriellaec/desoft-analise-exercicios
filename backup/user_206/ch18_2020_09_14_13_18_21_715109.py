def verifica_idade(idade):
    if idade >= 21:
        return("Liberado EUA e BRASIL")
    elif 18 <= idade < 21:
        return("Liberado BRASIL")
    else:
        return("Não está liberado")