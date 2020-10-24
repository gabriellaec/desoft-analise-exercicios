def verifica_idade(x):
    if (x<18):
        return "Não está liberado"
    if (18<=x<=21):
        return "Liberado BRASIL"
    if (x>21):
        return "Liberado no EUA e BRASIL"
