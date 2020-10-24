def verifica_progressao(n):
    pea=True
    peg=True
    a=False
    b=False
    pa=n[2]-n[1]
    pg=n[2]/n[1]
    if len(n)==0:
        return ("NA")
    if pea:
        for i in n-1:
            if n[i+1]-n[i]!=pa:
                pea=False
            else:
                a=True
    if peg:
        for i in n:
            if n[i+1]/n[i]!=pg:
                peg=False
            else:
                b=True
    if a:
        if b:
            return ("AG")
        else:
            return ("PA")
    elif b:
        return ("PG")
    else:
        return("NA")