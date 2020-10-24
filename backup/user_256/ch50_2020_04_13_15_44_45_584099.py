def junta_nome_sobrenome(nome, sobrenome):
    i = 0
    nova= []
    la[i] = nome[i] and sobrenome[i]
    while i< len(nome):
        nova.append(la[i])
        i+=1
    return nova