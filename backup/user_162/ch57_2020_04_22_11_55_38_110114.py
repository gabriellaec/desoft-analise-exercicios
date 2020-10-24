def verifica_progressao(l):
    if len(l)<2:
        return "NA"
    
    pa = True 
    pg = True
    ag = True
    
    r = l[1] - l[0]
    if l[0] == 0:
        i = 1
        while i < len(l):
            if l[i-1] + r != l[i]:
                pa = False
            i+=1
                
    else:
        q = l[1]/l[0]
        i = 1 
        while i < len(l):
            if l[i-1] + r != l[i] or l[i-1] * q != l[i]:
                ag = False
            if l[i-1] + r != l[i]:
                pa = False
            if l[i-1] * q != l[i]:
                pg = False
            i+=1
    
    if ag:
        return "AG"
    elif pa:
        return "PA"
    elif pg:
        return "PG"
    else:
        return "NA"