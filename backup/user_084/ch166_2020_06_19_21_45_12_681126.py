def total_do_semestre_por_bairro(DICI):
    gasto_DICI={}
    
    for c in DICI:
        gasto=0
        i=6
        while i<=11:
            gasto+=DICI[c][i]
            i+=1
        gasto_DICI[c]=gasto
    return gasto_DICI
            
        
        