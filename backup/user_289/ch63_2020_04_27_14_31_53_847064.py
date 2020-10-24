def pos_arroba(email):
    string = str(email)
    i = 0
    while i < len(string):
        if string[i] == "@":
            return i
        else:
            i += 1
def nome_usuario(email):
    return email[:i]