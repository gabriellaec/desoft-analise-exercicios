def classifica_idade(i):
i=int(input ('Entre com a idade: ')
    if i>=0 and i<=11:
        x='criança'
    elif i>=12 and i<=17:
        x='adolescente'
    elif i>=18:
        x='adulto'
    return x