def pos_arroba(email):
    i=0
    while i< len(email):
        if email[i] == '@':
            return i
        else:
            i+=1
            
def nome_usuario (palavra):
    verifica=pos_arroba(palavra)
    for i < verifica:
        palavra2=[]
        palavra2.append(palavra[i])
    return join.palavra2