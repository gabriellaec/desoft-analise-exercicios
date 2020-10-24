def pos_arroba(email):
    contador=0
    while contador<len(email):
        if email[contador]=="@":
            return contador
        contador+=1
def nome_usuario(email):
    i=0
    nome=[]
    while i<pos_arroba(email):
        nome.append(email[i])
        i+=1
    return ''.join(nome)