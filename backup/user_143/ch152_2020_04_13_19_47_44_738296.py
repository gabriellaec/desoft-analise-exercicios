def verifica_preco (s, d1, d2):
    p='a'
    preço=0
    for i,j in d1.items():
        if s==i:
            p=j
    for a,b in d2.items():
        if p==a:
            preço=b
    return preço
            