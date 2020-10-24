def verifica_idade(x):
    if x < 18:
        return "Não está liberado"
    elif x>=18<21:
        return  "Liberado BRASIL"
    else:
        return "Liberado EUA e BRASIL"