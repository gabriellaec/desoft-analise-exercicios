def total_do_semestre_por_bairro(dicio_gastos):
    dicio_final={}
    for bairro,gasto in dicio_gastos.items():
        soma = 0
        dicio_gastos[bairro]= gasto
        for i in range (len(gasto)-6,len(gasto)):
            soma+= (gasto[i])
            dicio_final[bairro]=soma
    return dicio_final
