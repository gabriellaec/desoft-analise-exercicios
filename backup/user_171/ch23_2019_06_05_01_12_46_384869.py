def verifica_idade(idade):
    if idade>21:
        resultado="Liberado EUA e BRASIL"
    elif idade>18:
        resultado="Liberado BRASIL"
    else:
        resultado="Não está liberado"
    return resultado
        