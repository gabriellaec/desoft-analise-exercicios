def classifica_idade(idade):
    if idade >= 18:
       return 'adulto'
    elif idade >= 12:
           return 'adolescente'
    else:
           return 'crianca'
print(classifica_idade(idade)) 