def pos_arroba(email):
    i = 0
    while i < len(email):
        if email[i] == '@':
            posicao = i + 1
            i = len(email)
        else:
            i += 1
    return posicao

a = 'jamesson1233@gmail.com'
print(pos_arroba(a))