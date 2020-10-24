def verifica_idade(idade):
    if idade>=18 and idade<21:
        print('Liberado no BRASIL')
    else: 
        print('Não está liberado')
    if idade >=21:
        print('Liberado EUA e BRASIL')