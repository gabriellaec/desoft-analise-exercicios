def classifica_idade(idade):
    if idade <= 11: 
        print('crianca')
    elif idade <= 17: 
        print('adolescente') 
    else:
        print('adulto')
        
idade = classifica_idade(10)