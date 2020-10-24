def junta_nome_sobrenome(lista_nome,lista_sobrenome):
    lista_vazia=[]
    cont=0
    while cont < len(lista_nome) and cont < len(lista_sobrenome):
        lista_vazia.append(lista_nome[cont]+' '+lista_sobrenome[cont])
        cont+=1
    return lista_vazia