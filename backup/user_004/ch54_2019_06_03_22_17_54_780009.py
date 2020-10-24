def junta_nome_sobrenome(listanome, listasobrenome):
    i=0
    lista=[]
    while len(listanome)>0:
        nome=listanome[i]+listasobrenome[i]
        listanome.remove(listanome[i])
        listasobrenome.remove(listasobrenome[i])
        i+=1
        lista.append(nome)
    return lista
