def verifica_idade(idade):
    if idade >= 21:
        print('Liberado EUA e BRASIL')
    if 18 <= idade < 21:
        print("Liberado BRASIL")
    if idade < 18:
        print("Não está liberado")
        