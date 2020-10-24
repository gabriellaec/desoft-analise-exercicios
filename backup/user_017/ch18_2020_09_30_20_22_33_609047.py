def verifica_idade(i):
    if i >=21:
        return "Liberado EUA e BRASIL" 
    else:
        if i>=18:
            return "Liberado BRASIL" 
        else:
            return "Não está liberado"