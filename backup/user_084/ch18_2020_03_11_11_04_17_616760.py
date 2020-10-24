def verifica_idade(i):
    if i>=21:
        return('liberado nos EUA e no Brasil')
    elif 21>i>=18:
        return('liberado Brasil')
    else i<18:
        return('NAO ESTA LIBERADO')