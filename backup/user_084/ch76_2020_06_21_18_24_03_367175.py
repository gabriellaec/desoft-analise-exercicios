def aniversariantes_de_setembro(DICI):
    DICI_final={}
    for c in DICI:
        if DICI[c][4]==9:
            DICI_final[c]=DICI[c]
    return DICI_final
        
        