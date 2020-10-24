def total_do_semestre_por_bairro(DICI):
    gasto_DICI={}
    i=6
    for c,v in DICI:
        gasto=0
        for i in range(11):
            gasto+=(DICI[c])[i]
        gasto_DICI[c]=gasto
    return gasto_DICI
            
        
        