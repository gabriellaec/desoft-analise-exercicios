def classifica_idade(idade)
    if idade >= 18:
       return 'adulto'
    elif idade >= 12:
           return 'adolescente'
        else:
           return 'crianca'
a = int(input('Qual sua idade?'))
print (classifica_idade(a)) 