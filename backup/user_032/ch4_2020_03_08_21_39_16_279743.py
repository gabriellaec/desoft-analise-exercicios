idade=int(input('Qual a sua idade:'))
def classifica_idade():
    if 0<=idade<=11:
        print('crianca')
    elif 12<=idade<=17:
        print('adolescente')
    else:
        print('adulto')
