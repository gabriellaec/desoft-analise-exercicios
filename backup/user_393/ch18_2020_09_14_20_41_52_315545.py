def verifica_idade(x):
    
    if 21 <= x:
        return "Liberdade EUA e BRASIL"

    elif 18 <= x <= 21:
        return "Liberdade BRASIL"

    else:
        return "Não está liberado"