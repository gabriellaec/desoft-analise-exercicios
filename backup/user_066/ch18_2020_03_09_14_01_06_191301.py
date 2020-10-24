def verifica_idade(idade):
    if idade <18:
        a = "Não está liberado"
    elif idade >=21:
        a = "Liberado EUA e BRASIL"
    else:
        a = "Liberado BRASIL"
    return a