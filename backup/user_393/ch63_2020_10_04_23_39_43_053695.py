def nome_usuario(str):
    i= 0
    while i < len(str):

        if str[i]== '@':
            break
        i= i + 1
    nome= str[0:i]
    return nome