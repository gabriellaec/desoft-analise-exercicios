def classifica_idade (c):
    if c>0 and c<=11:
        return 'crianca'
    elif 12<=c and 17>=c:
        return 'adolescente'
    else:
        return 'adulto'
c=int(input('idade de c'))

    