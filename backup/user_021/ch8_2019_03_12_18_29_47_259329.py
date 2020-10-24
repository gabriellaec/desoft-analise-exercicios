
def verifica_progressao(seq):
    qtds=len(seq)
    if qtds==2 and seq[1]!=0:        
        return "AG"
    elif qtds==2:
        return "PA"
    elif qtds==1:
        return "NA"
    else:
        i=0
        r=[]
        q=[]
        while i<(qtds-1):
            r.append(seq[i+1]-seq[i])
            if 0 not in seq:
                q.append(seq[i+1]/seq[i])
            i+=1
        i=0
        qtdq=len(q)
        qtdr=len(r)
        while i<qtdr:
            if r[1]==r[i]:
                testr=True
            else:
                testr=False
                break
            i+=1
        i=0
        while i<qtdq:
            if q[1]==q[i]:
                testq=True
            else:
                testq=False
                break
            i+=1
        if testr:
            return "PA"
        elif testq:
            return "PG"
        else:
            return "NA"