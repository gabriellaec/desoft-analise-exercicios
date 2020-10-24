def junta_nome_sobrenome(nome, sobrenome):
    i = 0
    nova_lista=[]
    while i < len(nome) or i < len(sobrenome):
        nova_lista.append(nome[i]+sobrenome[i])
        i += 1
    return nova_lista