perg_idade=int(input('qual sua idade:'))
def classifica_idade(i):
    i=perg_idade
    if i<=11:
        print ('crianca')
    elif i>=12 and i<=17:
        print('adolescente')
    else:
        print('adulto')
   
    