def calcula_valor_devido(emprestimo, meses, taxa):
    if (meses > 0) and (emprestimo > 0) and (taxa > 0):
        for i in range(0, meses, 1):
        	emprestimo = emprestimo*(1 + taxa)

        return emprestimo
    elif meses == 0:
        return emprestimo
    
    return 0
    