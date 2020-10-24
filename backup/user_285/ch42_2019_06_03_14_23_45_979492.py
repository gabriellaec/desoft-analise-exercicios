def quantos_uns(n):
    ocorrencias=0
    for i in n:
        if n[i] == "1":
            ocorrencias+=1
    return ocorrencias