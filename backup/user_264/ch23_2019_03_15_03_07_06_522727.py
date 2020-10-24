def verifica_idade(i):
    if i<18:
       return "Não está liberado"
    elif i<=21:
       return "Liberado Brasil"
    else:
       return "Liberado EUA e Brasil"