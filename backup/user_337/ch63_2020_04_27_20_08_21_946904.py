def nome_usuario(string):
    i = string.find('@')
    usuario = string[:i]
    return usuario