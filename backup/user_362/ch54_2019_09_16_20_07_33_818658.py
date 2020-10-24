def junta_nome_sobrenome(nome,sobrenome):
    nome=[]
    sobrenome=[]
    nome_sobre=[]
    i=0
    while i <len(nome) and len(sobrenome):
        nome_sobre.append(nome[i]+sobrenome[i])
        i+=1
    return nome_sobre
    