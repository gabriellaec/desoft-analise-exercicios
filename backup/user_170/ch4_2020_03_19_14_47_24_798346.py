
def classifica_idade(i):
    if 0 < i <= 11:
        return 'crianca'
    elif 12 <= i <= 17:
        return 'adolescente'
    else:
        return 'adulto'
print(classifica_idade(18))