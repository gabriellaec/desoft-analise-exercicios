def quantos_uns(n):
    i = 0
    qtd_1 = 0
    if len(n) == 1:
        if n == '1':
            return 1
        else:
            return 0 
    else:
        while i != len(n):
            if n[i] == '1':
                qtd_1 += 1
                i += 1
            else:
                i += 1
    return qtd_1