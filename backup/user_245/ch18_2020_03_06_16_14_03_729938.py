def maioridade(ano):
    if ano >= 21:
        return "Liberado EUA e BRASIL"
    elif ano >= 19:
        return "Liberado BRASIL"
    else:
        return "Não está liberado"