def calcula_valor_devido(emprestimo, meses, taxa):
    if meses > 0:
        i = 0
        while i < meses:
        	emprestimo = emprestimo*taxa
            
        return emprestimo
    