def total_do_semestre_por_bairro(dicio_gastos):
    dicio_final={}
    soma = 0
    for bairro,gasto in dicio_gastos.items():
        dicio_gastos[bairro]= gasto
        for i in range (0,len(gasto)-6):
            soma+= gasto[i]
        dicio_final[bairro]=soma
        return dicio_final