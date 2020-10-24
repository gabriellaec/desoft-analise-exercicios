def verifica_idade(idade):
    if idade >= 21:
        return 'Liberado EUA e BRASIL'
    
    elif idade >= 18:
        return 'Liberado BRASIL'
    
    else:
        return 'Não está liberado'

a= float(input("Digite a sua idade:")
print (verifica_idade(a))