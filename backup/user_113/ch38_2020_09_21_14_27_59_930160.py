def quantos_uns(n):
    vezes = 0
    x=0
    while x <= len(n):
        num = str(n)
        if num[x]==1:
            vezes += 1
        x += 1
    return vezes
        