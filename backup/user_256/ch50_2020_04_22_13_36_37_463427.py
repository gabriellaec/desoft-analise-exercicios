def junta_nome_sobrenome(nome, sobrenome):
    i = 0
    nova= []
    while i< len(nome):
        la = nome[i]+" "+sobrenome[i]
        nova.append(la)
        i+=1
    return nova