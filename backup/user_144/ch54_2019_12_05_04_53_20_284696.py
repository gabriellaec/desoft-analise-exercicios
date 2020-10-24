def junta_nome_sobrenome(nome,sobrenome):
    new_list = []
    for i in range(len(nome)):
        for e in range(len(sobrenome)):
            tudo = nome[i] +" "+sobrenome[e]
        new_list.append(tudo)
    return new_list