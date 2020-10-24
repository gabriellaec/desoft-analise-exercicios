def primeiras_ocorrencias (x):
    dic=[]
    i=0
    for e in x:
        if x[e] in x:
            i+=1
            
        