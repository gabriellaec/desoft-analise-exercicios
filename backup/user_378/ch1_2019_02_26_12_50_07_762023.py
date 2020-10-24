v=valor_emprestado
t=taxa_de_juros
n=número_de_meses
def calcula_valor_devido(v,t,n)
    t=t/100
    return v*(1+t)**n

