def bairro_mais_custoso(c):
    mais_caro=100000000
    for i in c:
        
        if c[i]< mais_caro:
            mais_caro = c[i]
        else:
            c[i]=mais_caro
        
    return mais_caro