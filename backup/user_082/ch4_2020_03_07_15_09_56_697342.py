def classifica_idade (idade):
    if idade<11:
        return 'crianca'
    elif 12<idade<17:
        return 'adolescente'
    else:
        return 'adulto'
print (classifica_idade(2))