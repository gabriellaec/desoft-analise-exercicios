def verifica_idade(idade):
    if idade < 18:
        return 'Nao esta liberado'
    elif idade < 21:
        return 'Liberado Brasil'
    else:
        return 'Liberdo EUA e Brasil'
    
