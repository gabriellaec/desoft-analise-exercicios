def pos_arroba(string):
    for i in range(0, len(string)):
        if string[i] == '@':
            return i
        
def nome_usuario(string):
    pos= pos_arroba(string)
    return string[:pos]