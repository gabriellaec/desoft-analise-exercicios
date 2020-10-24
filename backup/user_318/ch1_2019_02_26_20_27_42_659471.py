v=float(input('Qual foi o valor emprestado?'))
n=int(input('Quantos meses ja se passaram?'))
j=float(input('Qual foi a taxa de juros mensal? (lembre-se de que 10% se escreve como 1.1 e 5% como 1.05 etc)'))
def calcula_valor_devido(v,n,j):
    p=v*j**n
    return p
d=calcula_valor_devido(v,n,j)
print('Você deve o valor de', d)

