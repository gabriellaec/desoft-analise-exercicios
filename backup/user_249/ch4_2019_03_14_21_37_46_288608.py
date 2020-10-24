id=int(input('Qual sua idade? '))
def classifica_idade():
    if id<=11:
        return ('crianca')
    elif id<=17:
        return ('adolescente')
    else:
        return ('adulto')
print (classifica_idade())