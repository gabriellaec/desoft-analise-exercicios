def classifica_idade(idade):
    if idade<12:
        print('crianca')
    elif 11>idade<18:
        print('adolescente')
    elif idade>=18:
        print('adulto')
    return idade
    