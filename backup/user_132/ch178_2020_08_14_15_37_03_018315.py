def junta_nomes(nome_h,nome_m,sobrenome):
    resposta = []
    for t in sobrenome:
        for i in nome_h:
            resposta.append(i + ' ' + t)
        for i in nome_m:
            resposta.append(i + ' ' + t)
    return print(resposta)

    