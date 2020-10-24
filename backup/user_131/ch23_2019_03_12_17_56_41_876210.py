def verifica_idade(b):
    if b>21:
        return "Liberado EUA e BRASIL"
    elif 18<b and b<21:
        return "Liberado BRASIL"
    else:
        return "Não está liberado"
print(verifica_idade(15))