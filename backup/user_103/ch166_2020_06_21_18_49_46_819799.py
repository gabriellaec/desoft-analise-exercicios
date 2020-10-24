def total_do_semestre_por_bairro(dicio_gastos):
    dicio_final={}
    soma = 0
    for bairro,gasto in dicio_gastos.items():
        dicio_gastos[bairro]= gasto
        for i in range (0,len(gasto)-6,1):
            soma+= gasto[i:6:1]
            dicio_final[bairro]=soma
        return dicio_final
