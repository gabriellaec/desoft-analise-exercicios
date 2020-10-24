def classifica_idade(x):
    if x<=11:
        return 'crianca'
    elif x>=12 and x<=17:
        return 'adolesscente'
    else:
        return 'adulto'
print(classifica_idade(15))