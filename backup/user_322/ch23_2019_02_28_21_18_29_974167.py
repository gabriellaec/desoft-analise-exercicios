def verifica_idade(idade):
    if idade >= 21:
        return "Liberado EUA e BRASIL"
    if 18 <= idade < 21:
        return "Liberado BRASIL"
    if idade < 18:
        return "Nao está liberado"