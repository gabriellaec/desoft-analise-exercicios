def nome_usuario(string):
    lista_string = list(string)
    lista_nome = []
    for k in lista_string:
        if k != '@':
            lista_nome.append(k)
    string_nome = ''
    for v in lista_nome:
        string_nome += v
    return string_nome