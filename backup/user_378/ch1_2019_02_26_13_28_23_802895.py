def calcula_valor_devido(v,t,n):
    y=v*(1+t)**n
    return y
v=float(input('valor emprestado:'))
t=float(input('taxa de juros:'))
n=input('número de meses:')
t=t/100        
print('valor devido:', calcula_valor_devido(v,t,n))