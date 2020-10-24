def junta_nome_sobrenome(nome,sobrenome):
    i=0
    completo=[]
    a=0
    while i<len(nome):
        a=nome[i]+' '+sobrenome[i]
        completo.append(a)
        i+=1
    return completo