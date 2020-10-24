def classifica_idade(idade):
    if idade<12:
        return('crianca')
    if 12<=idade<18:
        return('adolescente')
    if idade>=18:
        return('adulto')

print(classifica_idade(12))
