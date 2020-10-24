def nome_usuario(s):
    p = s.find('@')
    r = s[:p]
    return r