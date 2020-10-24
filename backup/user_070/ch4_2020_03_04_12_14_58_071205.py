def classifica_idade(i):
    int(i)
    if i>=0 and i<=11:
        x='crianca'
    elif i>=12 and i<=17:
        x='adolescente'
    elif i>=18:
        x='adulto'
    return x