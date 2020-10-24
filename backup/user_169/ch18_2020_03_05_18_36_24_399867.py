def verifica_idade(p):
    if p>=21:
        return "Liberado EUA e BRASIL"

    elif p>=18 and p<21:
        return "Liberado BRASIL"
    
    else:
        return "Não está liberado"