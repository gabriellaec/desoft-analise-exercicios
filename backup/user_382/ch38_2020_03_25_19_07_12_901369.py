def quantos_uns(n):
    qntos = 0 
    n = str(n)
    for i in n:
        if i == '1':
            qntos += 1
    return qntos