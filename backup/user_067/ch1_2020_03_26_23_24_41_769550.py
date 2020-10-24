def calcula_valor_devido(emprestimo,meses, taxa):
    if meses > 0:
        devido = emprestimo*(taxa^meses)
        return devido
    