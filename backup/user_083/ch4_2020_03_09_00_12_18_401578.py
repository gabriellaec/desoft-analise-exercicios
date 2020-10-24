def   classifica_idade (idade) :

    if idade  <= 11:
           return 'crianca'
    else:
        if idade <=17 >=12:
            return 'adolescente'
        else:
            return 'adulto'
        
print(classifica_idade(10))
print(classifica_idade(15))
print(classifica_idade(30))