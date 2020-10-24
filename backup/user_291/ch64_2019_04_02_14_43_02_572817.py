def nome_usuario(a):
    i = 0 
    x = 0
    while i < len(a):
        if a[i] == "@":
            x = i
    nome = a[:x]
    return nome