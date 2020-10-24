def pos_arroba(x):
    i=0
    n=len(x)
    while i<n:
        if x[i]=="@":
            pos=i
        i+=1
    return pos

def nomedeusuário(email):
    pos=pos_arroba(email)
    return email[:pos]
