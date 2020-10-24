C=('valor emprestado')
n=('número de meses')
i=('taxa de juros')
def calcula_valor_devido(C,i,n):
    M=C*(1+i)**n
    return M