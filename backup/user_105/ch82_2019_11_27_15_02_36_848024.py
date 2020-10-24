def primeiras_ocorrencias (palavra):
    dicio = {}
    po = []
    cont = 0
    for i in palavra:        
        if i not in po:
            po.append(i)
            dicio[i]=cont
            
        cont+=1
            
    return dicio
    