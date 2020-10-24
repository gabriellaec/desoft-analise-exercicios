def junta_nome_sobrenome(nome, sobrenome):
    lista_nova=[]
    i=0
    for e in nome:
        for s in sobrenome:
            while i<len(nome):
                lista_nova.append(nome[i]+" "+sobrenome[i])
                i+=1
    return lista_nova