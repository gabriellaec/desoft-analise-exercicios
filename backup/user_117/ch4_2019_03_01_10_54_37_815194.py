def classifica_idade(pessoa):
    if pessoa<=11:
        print ('crianca')
    elif 12<=pessoa<=17:
        print ('adolescente')
    elif pessoa>=18:
        print ('adulto')
        
pessoa=int(input("Qual a idade?"))
print(classifica_idade(pessoa))