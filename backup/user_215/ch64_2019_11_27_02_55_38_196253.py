def nome_usuario(email):
    pos = 0
    while email[pos] != "@":
        pos += 1
    if email[pos] == "@":
        pos = pos
    print(email[0,pos])
    