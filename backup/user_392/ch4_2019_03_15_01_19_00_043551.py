def classifica_idade(x):
    if x <= 11:
        print ('criança')
    elif x >= 12 and x <= 17:
        print ('adolescente')
    else:
        print ('adulto')
 a = int(input('digite sua idade:'))
print(classifica_idade(a))