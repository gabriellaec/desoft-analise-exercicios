def classifica_idade(n):
    if n >= 18:
        return 'adulto'
    elif n <= 11:
        return 'crianca'
    else:
        return 'adolescente'
idade= int(input('qual a idade?'))
print (classifica_idade(idade))
        