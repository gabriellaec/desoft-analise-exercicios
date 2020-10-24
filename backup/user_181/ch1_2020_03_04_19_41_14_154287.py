def calcula_valor_devido(p,i,n):
    if n==0:
        s=p
        return s
    else:
        s=p(1+i)^n
        return s