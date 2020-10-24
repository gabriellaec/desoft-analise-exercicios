def calcula_valor_devido(p,i,n):
    s=p(1+i)^n
    if n==0:
        s=p
    else:
        return s