def classifica_idade(idade):
    if idade <= 11:
        print ('Você é uma crianca')
    elif idade >12 and idade <17:
        print ('Você já é adolescente')
    elif idade >= 18:
        print ('Você é adulto')
    return classifica_idade
