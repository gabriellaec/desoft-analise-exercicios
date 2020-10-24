def calcula_valor_devido (ve,nm,tj):
    if ve==0 or nm == 0 or tj==0 :
        r=ve
    else:
        r=ve*(1+tj)**nm
        return r
