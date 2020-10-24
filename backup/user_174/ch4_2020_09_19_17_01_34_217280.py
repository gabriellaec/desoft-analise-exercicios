def classifica_idade(x):
    if x <= 11:
        return 'crianca'
    else:
        if x>12 and x<17:
            return 'adolescente'
    else:
        if x>=18:
            return 'adulto'
print(classifica_idade(x))
        