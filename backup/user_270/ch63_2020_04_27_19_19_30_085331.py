def pos_arroba(s):
    i = 0
    while i < len(s):
        if s[i] == "@":
            break
        else:
            i+=1
    return i
def nome_usuario(s):
    s_user = s.split("@")
    return s_user[0]