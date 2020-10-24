def pos_arroba (string):
    i = 0
    while string [i] != "@":
        i += 1
    return i
    

def nome_usuario (i,string):
    t = string[:i]
    return t