def agrupa_por_idade(DICI_pessoa):
    DICI_faixa_etaria={'criança':[],'adolescente':[],'adulto':[],'idoso':[]}
    for c in DICI_pessoa:
        if DICI_pessoa[c]<=11:
            DICI_faixa_etaria[criança].append(c)
        if 12<=DICI_pessoa[c]<=17:
            DICI_faixa_etaria[adolescente].append(c)
        if 18<=DICI_pessoa[c]<=59:
            DICI_faixa_etaria[adulto].append(c)
        if DICI_pessoa[c]>=60:
            DICI_faixa_etaria[idoso].append(c)
        return DICI_faixa_etaria
    
        