def junta_nome_sobrenome(nome,sobrenome):
    listaconjunta=[]
    n=0
    while n<len(nome) and n<len(sobrenome):
        listaconjunta.append(nome[n]+' '+sobrenome[n])
        n+=1
    return listaconjunta