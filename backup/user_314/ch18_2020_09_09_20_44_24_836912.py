def verifica_idade (x):
    if(x>=18):
        if(x>=21):
            return "Liberado EUA e BRASIL"
        else:
            return "Liberado BRASIL"
    else:
        return "Não está liberado"