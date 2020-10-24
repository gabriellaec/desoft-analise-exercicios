def nome_usuario(string):
    nome = ''
    for i in range(0,len(string)+1):
        if '@' == string[i]:
            return nome
        else:
            nome += string[i]
    return nome