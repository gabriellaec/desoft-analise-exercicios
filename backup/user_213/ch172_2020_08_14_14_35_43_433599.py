def imprime_faixa(n):
    d=''
    if n>0:
        if n<18:
            d = 'jovem'
        if n>59:
            d = 'idoso'
        else:
            d = 'adulto'
    return d

        