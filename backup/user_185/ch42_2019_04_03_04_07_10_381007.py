def quantos_uns(número):
    i = 0
    soma = 0
    a = str(número)
    while i<len(a):
        if a[i:i+1] == 1:
            soma = soma + 1
            print(soma)
            i = i + 1