def primeiras_ocorrencias(string):
    dici={}
    i=0
    
   
    for c in string:
        if c not in dici:
            dici[c]=i
        i+=1
    return dici