def verifica_idade():
    idade: int(input('Quantos anos você tem? '))
    if idade < 18:
        return('Não está liberado')
    elif 18<idade<21:
        return('Liberado BRASIL')
    else:
        return('Liberado EUA e BRASIL')