def pos_arroba(x):
    i=0
    while x[i]!= "@":
        i+=1
    return i+1
def nome_usuario(email):
    return email[:pos_arroba(a)-1]