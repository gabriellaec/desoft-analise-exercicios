def verifica_idade(idade):
    if int(idade) >= 21:
        return "Liberado EUA e BRASIL"
    elif int(idade) >= 18:
        return "Liberado BRASIL"
    else:
        return "Não está liberado."
print(verifica_idade(idade))