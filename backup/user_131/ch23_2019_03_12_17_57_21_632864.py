def verifica_idade(b):
    if b>18 and b<21:
        return "Liberado BRASIL"
    elif b>21:
        return "Liberado EUA e BRASIL"
    else:
        return "Não está liberado"
print(verifica_idade(15))