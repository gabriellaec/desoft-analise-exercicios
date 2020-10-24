from sympy import solve
def resolve_equacao_1o_grau(a, b):
    equacao = solve(a*x + b)
    return equacao