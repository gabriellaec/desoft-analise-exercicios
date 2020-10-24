montante=int(input('De quanto dinheiro voce precisa?'))
meses=int(input('Em quantos meses vc irá pagar?'))
juros=input('vamos calcular a taxa de juros desse valor')
def calcula_valor_devido(Po, m):
    c=Po*(1.1)**m
    return c
print(calcula_valor_devido(montante,meses))