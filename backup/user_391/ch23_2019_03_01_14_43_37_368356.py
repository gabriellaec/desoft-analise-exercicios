def  verifica_idade(a):
    if a>21:
        return "Liberado EUA e BRASIL"
    elif a>18 and a<21:
        return "Liberado BRASIL"
    else:
        return "Não está liberado"
        