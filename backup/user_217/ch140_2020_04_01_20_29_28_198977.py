def faixa_notas(listas_notas):
    resposta = []
    a = 0
    b = 0
    c = 0
    for i in listas_notas:
        if i < 5:
            a += 1
        elif i >= 5 and i <= 7:
            b+= 1
        else:
            c += 1
    resposta.append(a)
    resposta.append(b)
    resposta.append(c)

    return resposta