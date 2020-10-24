perg_idade=int(input('qual sua idade:'))
def classifica_idade(perg_idade):
    y=perg_idade
    if y<=11:
        print ('crianca')
    elif y>=12 and y<=17:
        print('adolescente')
    else:
        print('adulto')
    return crianca, adolescente, adulto