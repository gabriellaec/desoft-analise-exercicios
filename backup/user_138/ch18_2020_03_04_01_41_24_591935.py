def verifica_idade(i):
    if i<18:
        permissao="Não está liberado"
    elif i<21:
        permissao="Liberado BRASIL"
    else:
        permissao="Liberado EUA e BRASIL"
    return permissao