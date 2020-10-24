def bairro_mais_custoso(DICI):
    maior=0
    bairro=''
    for c in DICI:
        gasto=0
        i=6
        while i<=11:
            gasto+=DICI[c][i]
            i+=1
        if gasto>maior:
            maior=gasto
            bairro=c
    return bairro
        
        
        