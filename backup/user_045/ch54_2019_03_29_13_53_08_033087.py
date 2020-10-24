def junta_nome_sobrenome(nome,sobre):
    i=0
    y=[]
    k=' '
    while i<len(nome):
        y.append(nome[i]+k+sobre[i])
        i+=1
    return y