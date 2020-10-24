def quantos_uns(n):
    vezes = 0
    x=0
    while x <= n:
        if n[x]==1:
            vezes += 1
        x += 1
    return vezes
        