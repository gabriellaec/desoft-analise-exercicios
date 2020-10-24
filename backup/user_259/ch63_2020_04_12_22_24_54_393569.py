def nome_usuario(palavra):
    i = 0
    while i<len(palavra):
        if palavra[i] == '@':
            return palavra[:i]
        else:
            i+=1