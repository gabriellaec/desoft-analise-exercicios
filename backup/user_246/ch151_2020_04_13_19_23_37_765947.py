def classifica_lista(l):
    decres=False
    cresc=False
    if len(l)<2:
        return ('nenhum')
    else:
        for i in range(1,len(l)):
            if l[i-1]>l[i]:
                decres=True
            else:
                cresc=True
    if cresc and decres:
        return ('nenhum')
    elif cresc and not decres:
        return ('crescente')
    else:
        return ('decrescente')
                