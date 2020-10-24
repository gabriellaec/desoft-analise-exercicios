def  verifica_idade(i):
    if (i>=21):
        return("Liberado nos EUA e Brasil.")
    elif (i>=18):
        return("Liberado no Brasil.")
    elif (i<18):
        return("Não está liberado")