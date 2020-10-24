def total_do_semestre_por_bairro(dicionario):
    soma_gastos = 0
    dic = {}
    for i in dicionario:
        a = 12
        while a >= 6:
            soma_gastos = dicionario[i[a]]
            a -= 1
        dic[i] = []
        dic[i].append(soma_gastos)