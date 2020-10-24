def verifica_idade(idade):
    if idade >= 21:
        return 'Liberado EUA e BRASIL'
    else:
        if idade >= 18:
            return 'Liberado BRASIL'
        else:
            return 'Nao esta liberado'
print (verifica_idade(17))