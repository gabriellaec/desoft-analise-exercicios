def classifica_idade (c):
    if c<=11:
        return 'crianca'
    elif 12<c and 17>=c:
        return 'adolescente'
    else:
        return 'adulto'
print (classifica_idade (c))

    