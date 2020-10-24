def verifica_idade(i):
    if i<=16:
       return "Não está liberado"
    elif i<=18:
       return "Liberado Brasil"
    else:
       return "Liberado EUA e Brasil"