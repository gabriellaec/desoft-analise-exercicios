def classifica_lista(n):
    cresc=True
    decr=True
    if len(n)<2:
        return('nenhum')
    for i in range(len(n)-1):
        if n[i+1]-n[i]>0:
            decr=False
        elif n[i+1]-n[i]<0:
            cresc=False
        else:
            return('nenhum')
    if decr:
        return('decrescente')
    elif cresc:
        return('crescente')
    else:
        return('nenhum')