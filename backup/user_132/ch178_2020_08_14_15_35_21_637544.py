def junta_nomes(a,b,c):
    resposta = []
    for t in c:
        for i in a:
            resposta.append(i + ' ' + t)
        for i in b:
            resposta.append(i + ' ' + t)
    return print(resposta)

    