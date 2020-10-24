def junta_nome_sobrenome(nome,sobrenome):
    i=0
    y=[]
    k=''
    while i < len(nome):
        y.append(nome[i]+k+sobrenome[i])
        i+=1
    return y
        
    