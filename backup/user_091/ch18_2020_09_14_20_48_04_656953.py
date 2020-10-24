def verifica_idade(a):
    
    if 18<=a<=21:
        return "Liberado BRASIL"
    elif a>=21:
        return "Liberado EUA e BRASIL"
    else:
        return "Não está liberado"

