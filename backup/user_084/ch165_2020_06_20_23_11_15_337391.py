def mais_populoso(BRASIL):
    POP=0
    for c in BRASIL:
        ESTADO=''
        TOTAL=0
        for v in BRASIL[c]:
            TOTAL+=BRASIL[c][v]
        if TOTAL>POP:
            POP=TOTAL
            ESTADO=v
        else:
            pass
    return ESTADO
            
            
            
            