def mais_populoso(BRASIL):
    POP=0
    for c in BRASIL:
        ESTADO='São Paulo'
        TOTAL=0
        for v in BRASIL[c]:
            TOTAL+=BRASIL[c][v]
        if TOTAL>POP:
            POP=TOTAL
            #ESTADO
        else:
            pass
    return ESTADO
            
            
            
            