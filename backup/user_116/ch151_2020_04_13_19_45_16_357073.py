def classifica_lista(x):
    if len(x)>=2:
        cre=[x[0]]
        de=[x[0]]
        ini1=x[0]
        ini2=x[0]
        for e in range(1,len(x)):
            if x[e]>ini1:
                cre.append(x[e])
                ini1=x[e]
            if x[e]<ini2:
                de.append(x[e])
                ini2=x[e]
        if de==x:
            return 'decrescente'
        elif cre==x:
            return 'crescente'
        else:
            return 'nenhum'
    else:
        return 'nenhum'