def pos_arroba(n):
    a = n.find('@')
    return a
def nome_usuario(x):
    b = pos_arroba(x)
    return x[0:b]