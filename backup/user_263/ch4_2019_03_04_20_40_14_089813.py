def classifica_idade(i):
    i=int(input('Digite a sua idade:'))
    if i<=11:
        return 'crianca'
    elif i<=17:
        return 'adolescente'
    else:
        return 'adulto'
    
