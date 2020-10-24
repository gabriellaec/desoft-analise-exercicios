def mais_populoso(BRASIL):
    POP=0
    ESTADO=''
    for c in BRASIL:
        TOTAL=0
        for v in BRASIL[c]:
            TOTAL+=BRASIL[c][v]
        if TOTAL>POP:
            POP=TOTAL
            ESTADO=c
        else:
            pass
    return ESTADO
            
            
            
            