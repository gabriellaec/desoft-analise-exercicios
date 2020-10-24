def junta_nome_sobrenome(nome, sobrenome):
    i=0
    nome_completo=[]
    while i<len(nome):
        nome_completo.append(nome[i]+' '+sobrenome[i])
        i+=1
    return nome_completo