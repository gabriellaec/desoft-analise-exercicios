idade=int(input('Qual é a sua idade?  '))
def classifica_idade(idade):
    if idade<12:
        return ('crianca')
    elif idade<18:
        return ('adolescente')
    else:
        return ('adulto')
print(classifica_idade(idade))
