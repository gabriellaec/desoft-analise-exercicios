def junta_nome_sobrenome(nome,sobre):
    i=0
    y=[]
    k=' '
    while i<len(nome):
        y.append(nome+k+sobre)
        i+=1
    return y