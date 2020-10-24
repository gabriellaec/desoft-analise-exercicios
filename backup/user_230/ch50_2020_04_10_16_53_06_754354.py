def junta_nome_sobrenome(nome, sobrenome):
    nome_completo=[]
    for i in range(len(nome) and len(sobrenome)):
        nome_completo.append(nome[i]+" "+sobrenome[i])
    return nome_completo

    