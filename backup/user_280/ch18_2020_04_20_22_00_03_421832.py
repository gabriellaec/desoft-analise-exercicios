def verifica_idade(idade):
    resultado = 'Bla'
    if idade >= 21:
        resultado = 'Liberado EUA e Brasil'
    if idade >= 18 and idade < 21:
        resultado = 'Liberado BRASIL'
    if idade < 18:
        resultado = 'Não está liberado'
    return str(resultado)