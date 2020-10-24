def classifica_idade (x):
    if x <= 11: 
        return ('Criança')

    elif 12 >= x <= 17:
        return ('Adolescentes')

    else:
        return ('Adulto')

idade = 20

print (classifica_idade(idade))
