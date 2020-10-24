def verifica_preco(t,d,c):
    if t in d:
        cor_referencia=d[t]
        if cor_referencia in c:
            p= c[cor_referencia]
            return p