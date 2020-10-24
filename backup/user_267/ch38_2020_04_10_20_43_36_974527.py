def quantos_uns(a):
    txn = str(a)
    num_em_a = len(txn)
    soma = 0
    i = 0
    while i < num_em_a:
        if txn[i] == '1':
            soma += 1
            i +=1
        else:
            i += 1
    return soma
    