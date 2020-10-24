def classifica_idade(i):
    if i<=11:
        return 'crianca'
    elif i<=17:
        return 'adolescente'
    else:
        return 'adulto'
i=int(input('Digite a sua idade:'))
print(classifica_idade(i))