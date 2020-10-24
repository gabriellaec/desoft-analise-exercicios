def quantos_uns(palavra):
    soma=0
    for c in palavra:
        if c=='1':
            soma+=1
    return soma
