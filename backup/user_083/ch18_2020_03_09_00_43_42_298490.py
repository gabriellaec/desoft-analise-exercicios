def  verifica_idade(idade):
    if idade >=21:
        return 'Liberado EUA e BRASIL'
    else:
        if idade >=18:
            return 'Liberado BRASIL'
        else:
            if idade < 18:
                return 'Não está liberado'
print(verifica_idade(9))
print(verifica_idade(19))
print(verifica_idade(29))