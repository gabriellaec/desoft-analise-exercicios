def classifica_idade(pessoa):
    if int(pessoa)<=11:
        return ('crianca')
    elif 12<=int(pessoa)<=17:
        return ('adolescente')
    elif int(pessoa)>=18:
        return ('adulto')
        
pessoa=input("Qual a idade?")
print(classifica_idade(pessoa))