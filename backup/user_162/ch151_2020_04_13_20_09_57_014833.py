def classifica_lista(l):
    if len(l) < 2:
        return "nenhum"
    t_cre = [l[0]]
    t_dec = [l[0]]
    for i in range(1,len(l)):
        if l[i] > l[i-1]:
            t_cre.append(l[i])
        elif l[i] < l[i-1]:
            t_dec.append(l[i])
        else:
            return "nenhum"
    if t_cre == l:
        return "crescente"
    elif t_dec == l:
        return "decrescente"
    else:
        return "nenhum"