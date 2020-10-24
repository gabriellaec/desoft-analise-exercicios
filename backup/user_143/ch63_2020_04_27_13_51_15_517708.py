def pos_arroba(s):
    a=s.find('@')
    return a
def nome_usuario(n):
    i=pos_arroba(n)
    nome=n[:i:1]
    return nome