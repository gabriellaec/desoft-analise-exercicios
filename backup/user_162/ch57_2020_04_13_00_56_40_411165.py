def verifica_progressao(l):
    if len(l)<2:
        return "NA"
    
    r = l[1] - l[0]
    comparapa = [l[0]]
    for i in range(1, len(l)):
        comparapa.append(comparapa[-1]+r)
        
    if l[0] == 0:
        if comparapa == l:
            return "PA"
            
    else:
        comparapg = [l[0]]
        q = l[1]/l[0]
        for i in range(1, len(l)):
            comparapg.append(comparapg[-1]*q)    
        if comparapa == l and comparapg == l:
            return "AG"
        elif comparapa == l:
            return "PA"
        elif comparapg == l:
            return "PG"
        else:
            return "NA"