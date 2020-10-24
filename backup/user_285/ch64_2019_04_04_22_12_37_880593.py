def pos_arroba(email):
    tamanho=len(email)
    i=0
    while i<tamanho:
        if email[i]=="@":
            return i
        i+=1
def nome_usuario(email):
    posicao=pos_arroba(email)
    nome=email[0:posicao]
    return nome       
           
        