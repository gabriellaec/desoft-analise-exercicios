def aniversariantes_de_setembro(DICI):
    DICI_final={}
    for c in aniversariantes_de_setembro:
        if DICI[c][4]==9:
            DICI_final[c]=DICI[c]
        else:
            pass
    return DICI_final
        
        