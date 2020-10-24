def quantos_uns(n):
    n = str(n)
    i=0
    frequencia=0
    while i < len(n):
        if n[i] == '1':
            frequencia+=1
    return frequencia