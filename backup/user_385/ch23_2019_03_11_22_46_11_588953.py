i = int(input('Quantos anos tem?'))
def verifica_idade(i):
    if i>21:
        return 'Liberado EUA e BRASIL'
    elif i<18:
        return 'Não está liberado'
    else:
        return 'Liberado BRASIL'
print (verifica_idade(i))
