def total_do_semestre_por_bairro(x):
    dicio2 = {}
    for i in x:
        a=x[i][5]+x[i][6]+x[i][7]+x[i][8]+x[i][9]+x[i][10]+x[i][11]
        dicio2[i]=a
        
    return dicio2