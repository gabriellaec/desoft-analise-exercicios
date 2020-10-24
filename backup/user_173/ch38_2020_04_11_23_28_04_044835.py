def quantos_uns (n):
    quantidade = 0
    n = str(n)
    for i in n:
        if i == '1':
            quantidade += 1
    return quantidade            