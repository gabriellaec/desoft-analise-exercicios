def calcula_valor_devido(emprestimo, meses, taxa):
    if meses > 0:
        devido = emprestimo*(1 + taxa^meses)
        return devido
    