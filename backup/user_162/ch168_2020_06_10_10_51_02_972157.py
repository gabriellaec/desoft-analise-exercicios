def login_disponivel(n, lis):
    num = []
    lis1 = []
    nomesrep = []
    for nome in lis:
        lis1.append(nome[:-1])
        if nome == n:
            nomesrep.append(nome)
    for nome in lis1:
        num.append(lis1.count(nome))
    if n in nomesrep:
        n = n + "{}".format(max(num)+1)
    return n
