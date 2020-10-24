def quantos_uns(n):
    n = str(n)
    c = len(n)
    i = 0
    ocorrencias = 0
    while i < c:
        if n[i] == '1':
            ocorrencias += 1
            i += 1
        else:
            i +=1
    return ocorrencias