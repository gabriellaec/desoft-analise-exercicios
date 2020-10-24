def nome_usuario(email):
    i = 0
    palavra = 'aa'
    while i < len(email):
        if email[i] == "@":
            return email[:i]
        i+=1
    