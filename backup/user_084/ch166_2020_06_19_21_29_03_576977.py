def total_do_semestre_por_bairro(DICI):
    gasto_DICI={}
    i=6
    for c in DICI:
        gasto=0
        while i<=11:
            gasto+=(DICI[c])[i]
            i+=1
        gasto_DICI[c]=gasto
    return gasto_DICI
            
        
        