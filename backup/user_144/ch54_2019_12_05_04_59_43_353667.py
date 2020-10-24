def junta_nome_sobrenome(nome,sobrenome):
    new_list = []
    for i in range(len(nome)):
        for i in range(len(sobrenome)):
            tudo = nome[i] + " " + sobrenome[i]
            new_list.append(tudo)
    return new_list