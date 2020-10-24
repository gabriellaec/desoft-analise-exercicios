def junta_nome_sobrenome(nome, sobrenome):
    i = 0
    nova= []
    while i< len(nome):
        nova[i] = (nome[i] and sobrenome[i])
        i+=1
    return nova