def nome_usuario(string):
    index = 0
    lista_string = list(string)
    for k in lista_string:
        index += 1
        if k == '@':
            pos = index - 1
    nome = ''
    i = 0
    while i <= pos:
        nome += lista_string[i]
        i+=1
    return nome