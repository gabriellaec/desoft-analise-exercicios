def calcula_valor_devido(emprestimo, meses, taxa):
    if (meses > 0) and (emprestimo > 0) and (taxa > 0):
        i = 0
        while i < meses:
        	emprestimo = emprestimo*taxa
            
        return emprestimo
    elif meses == 0:
        return emprestimo
    
    return 0
    