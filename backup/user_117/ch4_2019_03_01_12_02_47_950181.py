def classifica_idade(pessoa):
    if pessoa<=11:
        return ('crianca')
    elif 12<=pessoa<=17:
        return ('adolescente')
    elif pessoa>=18:
        return ('adulto')
        
pessoa=input("Qual a idade?")
print(classifica_idade(pessoa))