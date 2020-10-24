def pos_arroba(email):
    i = 0
    posicao = -1 #nao colocar 0, colocar -1 pois é a convenção que não achei a posição
    while i < len(email):
        if(email[i]=="@"):
            posicao = i
        i = i + 1
    return posicao

def nome_usuario(email):
    posicaoA = pos_arroba(email)
    i = 0
    nome = []
    while(i < posicaoA):
        nome.append(email[i])
        i = i + 1
        nome = "".join(nome) #junta a lista de letras separadas por espaços
        return nome

print(nome_usuario("luiz@insper.com"))
