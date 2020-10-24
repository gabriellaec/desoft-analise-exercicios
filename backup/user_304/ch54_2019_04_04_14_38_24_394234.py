def junta_nome_sobrenome (nome, sobrenome):
    completo=[]
    i=0
    while i<len(nome) and i<len(sobrenome):
        n=nome[i]+''+sobrenome[i]
        completo.append(n)
        i+=1
    return completo 