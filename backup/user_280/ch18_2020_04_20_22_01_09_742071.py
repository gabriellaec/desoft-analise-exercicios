def verifica_idade(idade):
    resultado = 'Bla'
    if int(idade) >= 21:
        resultado = 'Liberado EUA e Brasil'
    if int(idade) >= 18 and idade < 21:
        resultado = 'Liberado BRASIL'
    if int(idade) < 18:
        resultado = 'Não está liberado'
    return str(resultado)