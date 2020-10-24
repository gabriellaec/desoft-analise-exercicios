def classifica_idade(n):
    if n<=11:
        return 'crianca'
    elif n>=12 and n<=17:
        return 'adolescente'
    else:
        return 'adulto'
n= int(input('qual a classificacao da idade?'))
print(classifica_idade(n))
        