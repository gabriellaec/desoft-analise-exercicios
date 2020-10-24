erro = 0
for x in range (91):
    seno = (4*x*(180 - x))/ (40500 - x*(180-x))
    formula = math.sin(x)
    diferenca = seno - formula
    if abs(diferenca) > erro:
        erro = diferenca
print(erro)
        