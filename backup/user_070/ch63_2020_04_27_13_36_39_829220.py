def pos_arroba(s):
    return s.find('@')
def nome_usuario(s):
    x = ''
    for i in range(pos_arroba(s)):
        x = x + s[i]
    return x