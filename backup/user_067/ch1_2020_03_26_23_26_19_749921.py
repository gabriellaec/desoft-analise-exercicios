def calcula_valor_devido(emprestimo, meses, taxa):
    if meses > 0:
        devido = float(emprestimo)*(1 + taxa^float(meses))
        return devido
    