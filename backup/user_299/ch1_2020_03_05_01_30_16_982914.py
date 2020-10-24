v = float(input("Digite o valor do emprestimo:"))
m = int(input("Digite em quantos meses deseja pagar o emprestimo:"))
t = float(input("Digite o valor da taxa de juros:"))

def calcula_valor_devido(v, m, t):
    M = v*((1+t)**m)
    return M
