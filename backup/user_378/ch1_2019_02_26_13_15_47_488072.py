def calcula_valor_devido(v,t,n):
    y=v*(1+t)**n
    return y
v=float(input('valor emprestado:'))
t=float(input('taxa de juros:'))
n=float(input('número de meses:'))
t=t/100        
print('montante com juros compostos:', calcula_valor_devido(v,t,n))