def verifica_idade(idade) :
    if idade >= 21:
        return 'Liberado EUA e BRASIL'
    elif idade >= 18:
        return 'LIBERADO BRASIL'
    else:
        return 'NAO ESTA LIBERADO'
idade= int(input ('AGE: '))
resultado = verifica_idade(idade)
print(resultado)
