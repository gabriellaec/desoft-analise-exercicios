def verifica_idade(i):
    if i<18:
       return "Não está liberado"
    elif i<=21:
       return "Liberado BRASIL"
    else:
       return "Liberado EUA e BRASIL"