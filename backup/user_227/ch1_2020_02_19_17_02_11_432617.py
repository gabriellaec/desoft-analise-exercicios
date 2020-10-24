valor_emprestado: v
número_de_meses: n
taxa_de_juros:p

def calcula_valor_devido(v, p, n):
    return(v*(1+p/100)**n)
