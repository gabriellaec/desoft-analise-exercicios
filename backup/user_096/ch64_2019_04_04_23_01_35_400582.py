def nome_usuario(email):
    i=0
    while True:
        if email[i] != '@':
            i += 1
        elif email[i] == '@':
            return email[:i:1]
            break
