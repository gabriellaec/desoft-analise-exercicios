v=valor_emprestado
t=taxa_de_juros
n=número_de_meses
def calcula_valor_devido(v,t,n)
    y=int(v)*(1+int(t))**int(n)
    return y
